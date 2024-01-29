# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet  # Add the import for ProductViewSet
from rest_framework.authtoken.views import obtain_auth_token
path('auth', obtain_auth_token, name = 'api_token_auth'),

app_name = 'api'
router = DefaultRouter()
router.register('products', ProductViewSet)  # Register the ProductViewSet

urlpatterns = [
    path('', include(router.urls)),
]
