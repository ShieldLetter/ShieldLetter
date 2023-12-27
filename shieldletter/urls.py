from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

appname="shieldletter"

urlpatterns = [
    path("", views.index, name="index"),
    path("board", views.index, name="index"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("board/<int:id>", views.board_detail, name="board_detail"),
    path("board_write/", views.board_write, name="board_write"),
]

# 이미지 URL설정
urlpatterns += static(settings.UPLOAD_URL, document_root=settings.UPLOAD_ROOT)