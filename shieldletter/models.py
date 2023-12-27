from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=30, primary_key=True)
    user_pw = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.username

class Admin(models.Model):
    admin_id = models.CharField(max_length=30, primary_key=True)
    admin_pw = models.CharField(max_length=100)
    admin_name = models.CharField(max_length=50)
    def __str__(self):
        return self.admin_name

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    views = models.IntegerField(default=0)
    file = models.ImageField(upload_to='upload/',null=True)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title

