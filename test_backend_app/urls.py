from django.urls import path
from .views import Listar, Detail
from rest_framework.authtoken import views

urlpatterns = [
    path('list', Listar.as_view(), name='listar'),
    path('detail', Detail.as_view(), name='detail'),
    path('givme_token', views.obtain_auth_token, name='givme_token')
    
]