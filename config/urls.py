from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # 관리자 페이지를 유추하기 어렵게 수정
    path("shieldletter-hidden-panel/", admin.site.urls),
    path('', include('shieldletter.urls')),
]
