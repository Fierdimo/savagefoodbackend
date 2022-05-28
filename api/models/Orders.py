import uuid
from django.db import models

class Orders(models.Model):
    
    
    class Rating(models.IntegerChoices):
        EXCELENT = 5
        GOOD = 4
        REGULAR = 3
        MEDIOCRE = 2
        FORGET_ME = 1
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(help_text='Identificación del usuario', blank=False )
    user_alternate_id = models.CharField(help_text='Identificacion usuario no registrado', max_length=50)  
    delivery_id = models.UUIDField(help_text='Identificación del usuario', blank=False)
    total_value =models.IntegerField(help_text='Total a pagar')
    is_active = models.BooleanField(help_text='Envío aprovado', default=False)
    paid = models.BooleanField(help_text='Pago', default=False)
    rating = models.IntegerField(choices=Rating.choices, help_text='Calificación del servicio', default=5)
    order_list = models.JSONField(help_text='Pedido', encoder=None, decoder=None)

        
    def __str__(self):
        return self.name