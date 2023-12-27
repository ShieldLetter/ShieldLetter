from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def board(request):
    return render(request, 'board.html')

def board_write(request):
    return render(request, 'board_write.html')