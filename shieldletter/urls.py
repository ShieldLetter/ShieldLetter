from django.contrib import admin
from django.urls import path
from . import views

appname="shieldletter"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("board", views.board, name="board"),
    
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>',views.board, name="board"),
    path("board_write", views.board_write, name="board_write")
]
