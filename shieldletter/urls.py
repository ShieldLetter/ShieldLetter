from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.views.decorators.cache import never_cache
from .views import CustomLoginView


appname="shieldletter"

urlpatterns = [ # login 수정
    path("", never_cache(views.index), name="index"),
    path("login/", CustomLoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("signup/", views.signup, name="signup"),
    path("board/<int:id>", views.board_detail, name="board_detail"),
    path("board_write/", views.board_write, name="board_write"),
    path("board/<int:id>/update", views.board_update, name="board_update"),
    path("board/<int:id>/delete", views.board_delete, name="board_delete"),
]

# 이미지 URL설정
urlpatterns += static(settings.UPLOAD_URL, document_root=settings.UPLOAD_ROOT)