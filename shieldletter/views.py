from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.core.paginator import Paginator
from .forms import UserForm
from django.http import FileResponse, Http404
from django.conf import settings
from django.db.models import Max
import os


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

# 회원가입
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

# 게시글 상세
@never_cache
def board_detail(request, id):
    board = Board.objects.get(pk=id)
    
    if board.file and hasattr(board.file,'url'):
        file_url = board.file.url
    else:
        file_url = None
    
    # 조회수 증가
    board.views += 1
    board.save()
    
    return render(request, 'board_detail.html', {'board':board, 'file_url':file_url})

# 게시글 생성
# @login_required
def board_write(request):
    if request.method == 'POST':
        file = request.FILES.get('file') 
        if file:
            new_article = Board.objects.create(
                admin_id = 'admin', # 로그인 구현 전까지 임시
                category = request.POST['category'],
                title = request.POST['title'],
                content = request.POST['content'],
                file = file,
            )
        else:
            new_article = Board.objects.create(
                category = request.POST['category'],
                title = request.POST['title'],
                content = request.POST['content'],
            )
        return redirect('index')
    return render(request, 'board_write.html')

# 파일 다운로드
def download_file(request, path):
    if not path:
        raise Http404
    file_path = os.path.join(settings.UPLOAD_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = FileResponse(fh, content_type='application/octet-stream')
            return response
    else:
        raise Http404

# 게시글 수정
def board_update(request, id):
    board = Board.objects.get(pk=id)
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

# 게시글 삭제
def board_delete(request, id):
    board = Board.objects.get(pk=id)
    board.is_deleted = True
    board.save()
    return redirect('index')