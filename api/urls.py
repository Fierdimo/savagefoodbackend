from django.urls import path, include
from .routers import router
from .views.users import NewCustomer, NewAdmin, CustomAuthToken, LogoutView


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include(router.urls)),
    path('givme_token/', CustomAuthToken.as_view(), name='givme_token'),
    path('newadmin/', NewAdmin.as_view(), name='newadmin'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)