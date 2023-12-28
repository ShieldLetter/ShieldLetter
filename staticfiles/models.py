from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, user_id, name, phone_num, email, password=None):
        if not user_id:
            raise ValueError('아이디는 필수입니다.')
        if not name:
            raise ValueError('이름은 필수입니다.')
        if not phone_num:
            raise ValueError('전화번호는 필수입니다.')
        if not email:
            raise ValueError('이메일은 필수입니다.')

        user = self.model(
            user_id=user_id,
            name=name,
            phone_num=phone_num,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, name, phone_num, email, password):
        user = self.create_user(
            user_id=user_id,
            password=password,
            name=name,
            phone_num=phone_num,
            email=self.normalize_email(email),
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    user_id = models.CharField(verbose_name='아이디', max_length=30, unique=True, primary_key=True)
    password = models.CharField(verbose_name='비밀번호', max_length=100)
    name = models.CharField(verbose_name='이름', max_length=50)
    phone_num = models.CharField(verbose_name='전화번호', max_length=20)
    email = models.EmailField(verbose_name='이메일', max_length=100, unique=True)
    date_joined = models.DateTimeField(verbose_name='가입일', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='마지막 로그인', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name', 'phone_num', 'email']

    objects = MyUserManager()

    def __str__(self):
        return self.user_id

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Admin(models.Model):
    admin_id = models.CharField(max_length=30, primary_key=True)
    admin_pw = models.CharField(max_length=100)
    admin_name = models.CharField(max_length=50)
    def __str__(self):
        return self.admin_name

class Board(models.Model):
    no = models.IntegerField(default=0) # 게시글 번호
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    views = models.IntegerField(default=0)
    file = models.ImageField(upload_to='upload/%Y/%m/%d',null=True) # 파일 업로드 시 날짜별로 분류되어 저장
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False) # 게시글 삭제 플래그 처리를 위함 
    
    def __str__(self):
        return self.title

