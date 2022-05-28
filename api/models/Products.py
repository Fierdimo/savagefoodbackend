import uuid
from django.db import models

class Products(models.Model):
    
    class Category_group(models.IntegerChoices):
       NONE = 0
       HAMBURGUER = 1
       PIZZA = 2
       TACO = 3
       DRINK = 4
    
    class Qualification(models.IntegerChoices):
        EXCELENT = 5
        YUM = 4
        REGULAR = 3
        YUK = 2
        UGH = 1
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)   
    name = models.CharField(max_length=50, unique=True, help_text='Nombre')
    description = models.CharField(max_length=250, blank=True, help_text='Descripción')
    image = models.FileField(help_text='Imagen del producto', upload_to='assets')
    price = models.IntegerField(blank=False, default=0, help_text='Valor del producto')
    qualification = models.IntegerField(choices=Qualification.choices, help_text='Calificación del producto', default=5)
    reviewers = models.IntegerField(help_text='Cantidad de reviews', default=0)
    category = models.IntegerField(choices = Category_group.choices, default=0, help_text='Categoría')
    visible = models.BooleanField(help_text='Visible en el menu', default=True)
        
    def __str__(self):
        return self.name