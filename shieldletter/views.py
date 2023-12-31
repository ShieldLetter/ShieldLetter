from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.core.paginator import Paginator
from .forms import UserForm
from django.conf import settings
from django.db.models import Max
import os
from django.contrib import messages
from django.contrib.auth.views import LoginView   # 추가
from axes.handlers.proxy import AxesProxyHandler

# 메인 - 게시글 리스트
def index(request):
    boardlist = Board.objects.filter(is_deleted=False).order_by('-date')
    for i, board in enumerate(reversed(boardlist), start=1):
        board.no = i
        board.save()

    paginator = Paginator(boardlist, 10)
    page_number = request.GET.get('page')
    boardlist = paginator.get_page(page_number)

    return render(request, 'index.html', {'boardlist': boardlist})

# 로그인
class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request=request,
            username=username,
            password=password,
        )

        if user is not None:
            user.backend = 'axes.backends.AxesStandaloneBackend'
            login(request, user)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locked = AxesProxyHandler.is_locked(request=self.request)
        attempts = AxesProxyHandler.get_failures(request=self.request)
        context['locked'] = locked
        context['attempts'] = attempts//2
        return context

# 회원가입
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

# 게시글 상세
def board_detail(request, id):
    board = get_object_or_404(Board, pk=id, is_deleted=False) # 삭제된 게시글의 경우 404에러 발생
    
    if board.file and hasattr(board.file,'url'):
        file_url = board.file.url
    else:
        file_url = None
    
    # 조회수 증가
    board.views += 1
    board.save()
    
    return render(request, 'board_detail.html', {'board':board, 'file_url':file_url})

# 게시글 생성
@login_required
def board_write(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            file = request.FILES.get('file')
            user = request.user
            if file:
                new_article = Board.objects.create(
                    name = user, 
                    category = request.POST['category'],
                    title = request.POST['title'],
                    content = request.POST['content'],
                    file = file,
                )
            else:
                new_article = Board.objects.create(
                    name = user,
                    category = request.POST['category'],
                    title = request.POST['title'],
                    content = request.POST['content'],
                )
            return redirect('index')
        return render(request, 'board_write.html')
    else:
        return redirect('index')

# 게시글 수정
@login_required
def board_update(request, id):
    board = Board.objects.get(pk=id)
    if request.user.is_superuser:
        if request.method == 'POST':
            file = request.FILES.get('file') 
            if file:
                board.file = file
            board.category = request.POST['category']
            board.title = request.POST['title']
            board.content = request.POST['content']
            board.save()
            return redirect('index')
        return render(request, 'board_update.html', {'board':board})
    else:
        return redirect('index')

# 게시글 삭제
@login_required
def board_delete(request, id):
    if request.user.is_superuser:
        board = Board.objects.get(pk=id)
        board.is_deleted = True
        board.save()
        return redirect('index')
    else:
        return redirect('index')
