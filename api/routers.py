from .views.products import ProductView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('products', ProductView, basename='products')
