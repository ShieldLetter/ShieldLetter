from django.shortcuts import render
from .models import *

def index(request):
    # 모든 board를 가져와 postlist에 저장합니다
    boardlist = Board.objects.all()
    # index.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'index.html', {'boardlist':boardlist})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def board(request, id):
    # 게시글(Post) 중 id를 이용해 하나의 게시글(post)을 검색
    post = Post.objects.get(id=id)
    # board.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져온다.
    return render(request, 'board.html', {'post':post})

def board_write(request):
    return render(request, 'board_write.html')