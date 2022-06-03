from django.db import models

class Toy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, default='', blank=False)
    description = models.CharField(max_length=250, default='', blank=True)
    toy_category = models.CharField(max_length=50, default='', blank=False)
    was_included_in_home = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

