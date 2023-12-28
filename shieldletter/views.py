from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# 메인 - 게시글 리스트
def index(request):
    boardlist = Board.objects.all().order_by('-date')
    
    # 페이징 처리
    paginator = Paginator(boardlist, 5)
    page_number = request.GET.get('page')
    boardlist = paginator.get_page(page_number)  
    
    return render(request, 'index.html', {'boardlist':boardlist})

# 로그인
# def login(request):
#    return render(request, 'login.html')

# 회원가입
def signup(request):
    return render(request, 'signup.html')

# 게시글 상세
def board_detail(request, id):
    board = Board.objects.get(pk=id)
    
    # 조회수 증가
    board.views += 1
    board.save()
    
    return render(request, 'board_detail.html', {'board':board})

# 게시글 생성
@login_required
def board_write(request):
    if request.method == 'POST':
        file=request.FILES.get('file') 
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
