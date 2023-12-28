from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import signup

appname="shieldletter"

urlpatterns = [
    path("", views.index, name="index"),
    path("board", views.index, name="index"),
    path("login", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path("signup", views.signup, name="signup"),
    path("board/<int:id>", views.board_detail, name="board_detail"),
    path("board_write/", views.board_write, name="board_write"),
    path('admin', admin.site.urls),
    path('signup/', signup, name='signup'),
    

]

# 이미지 URL설정
urlpatterns += static(settings.UPLOAD_URL, document_root=settings.UPLOAD_ROOT)