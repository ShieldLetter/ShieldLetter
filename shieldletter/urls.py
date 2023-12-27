from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

appname="shieldletter"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path("signup", views.signup, name="signup"),
    path('board/<int:id>',views.board, name="board"),
    path("board_write", views.board_write, name="board_write")
]
