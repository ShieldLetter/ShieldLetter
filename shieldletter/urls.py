from django.contrib import admin
from django.urls import path
from . import views

appname="shieldletter"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("board", views.board, name="board"),
]
