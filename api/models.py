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

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    class User_group(models.IntegerChoices):
        ADMIN = 0       # Encargado del area
        CHECKER = 1     # Encargado de la caja
        DELIVERY = 2    # Encargado de llevar el servicio a domicilio
        ATTENDANT = 3   # Encargado del publico en el lugar
        CUSTOMER = 4    # Comensal

    id = models.SmallAutoField(primary_key=True)
    username = models.CharField('Username', max_length=20, unique=True)
    password = models.CharField('Password', max_length=30)
    name = models.CharField('Name', max_length=30)
    last_name = models.CharField('Name', max_length=30)
    email = models.EmailField('Email', max_length=100)
    address = models.CharField('Dirección', max_length=250, default="")
    user_group = models.IntegerField("Grupo", choices=User_group.choices)
    active_order = models.JSONField(
        "Pedido actual", encoder=None, decoder=None, blank=True)
    order_story = models.JSONField(
        "Historial de pedidos", encoder=None, decoder=None, blank=True, )

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'
class Products(models.Model):
    class Rating(models.IntegerChoices):  # Una especie de Yum Score
        TERRIBLE = 1
        YUCK = 2
        OK = 3
        YUM = 4
        EXCELENT = 5

    id = models.SmallAutoField(primary_key=True)
    product_name = models.CharField(
        help_text='Nombre del producto', max_length=50, default='')
    description = models.CharField(
        help_text='Descripción del producto', max_length=200, default='')
    value = models.IntegerField(help_text='Precio de venta', default=0)
    image_url = models.SlugField("Dirección de imagen", max_length=250)
    rating = models.IntegerField(
        "Calificación", choices=Rating.choices)    
class Orders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_list = models.JSONField(
        "Lista de productos", encoder=None, decoder=None)
    total_value = models.IntegerField("Valor total", default=0)
    user = models.CharField("Usuario adscrito", max_length=50)
    created = models.DateField("Fecha de creación", auto_now_add=True)
    modified = models.DateTimeField("fecha de modificación", auto_now=True)
    is_active = models.BooleanField("Pedido activo", default=True)
    on_delivery = models.BooleanField("Pedido en camino", default=False)
    paid = models.BooleanField("Pedido pago", default=False)
