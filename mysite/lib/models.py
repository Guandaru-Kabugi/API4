from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from datetime import date
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError("You need an email")
        if not username:
            raise ValueError('You need a username')
        user = self.model(email=self.normalize_email(email),username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,password):
        user = self.create_user(email=self.normalize_email(email),username=username,password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class User(AbstractUser):
    email = models.EmailField(unique=True,null=False,max_length=100,verbose_name='email')
    date_of_birth = models.DateField(default=date.today)
    username = models.CharField(max_length=50, unique=True,verbose_name='username')
    age = models.IntegerField(default=0)
    phone_number = PhoneNumberField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
    
    def __str__(self):
        return self.username
class Author(models.Model):
    name = models.CharField(max_length=150,null=False,verbose_name='First and Last Name')
    email = models.EmailField(unique=True,null=False)
class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name='title')
    content = models.TextField()
    publication_year = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)