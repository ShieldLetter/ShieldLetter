from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput, help_text="비밀번호를 다시 입력해주세요.")

    class Meta:
        model = User
        fields = ('user_id', 'password1', 'password2', 'name', 'phone_num', 'email')