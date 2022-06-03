from .views.products import ProductView
from .views.orders import OrderView
from .views.users import UserView, NewCustomer
from rest_framework import routers


router = routers.DefaultRouter()
router.register('products', ProductView, basename='products')
router.register('order', OrderView, basename='order')
router.register('user', UserView, basename='user')
router.register('newuser', NewCustomer, basename='newuser')
