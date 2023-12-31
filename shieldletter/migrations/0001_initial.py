# Generated by Django 3.2.19 on 2024-01-01 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='아이디')),
                ('password', models.CharField(max_length=100, verbose_name='비밀번호')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('phone_num', models.CharField(max_length=20, verbose_name='전화번호')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='이메일')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='마지막 로그인')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('no', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('file', models.ImageField(null=True, upload_to='upload/%Y/%m/%d')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=30)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
