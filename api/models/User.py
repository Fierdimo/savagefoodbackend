import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password



class UserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Group(models.IntegerChoices):
        Customer = 0
        Admin = 1
        Checker = 2
        Delivery = 3
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(help_text='Username', max_length = 15, unique=True)
    password = models.CharField(help_text='Password', max_length = 256)
    name = models.CharField(help_text='Name', max_length = 30)
    last_name = models.CharField(help_text='Lastname', max_length= 40)
    email = models.EmailField(help_text='Email', max_length = 100)
    group = models.IntegerField(choices=Group.choices, help_text='Tipo de usuario', default=0)
    option = models.CharField(help_text='Ultima accion', default='', max_length=10)

    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        if not self.option == 'edit':
            self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD = 'username'