from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView, ProductCreateView, PostUpdateView, PostDeleteView
from django.urls import path
from .views import ContactFormView

app_name = 'itreporting'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact', ContactFormView.as_view(), name='contact'),
    path('products/', views.product, name='products'),
    path('details/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', PostUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', PostDeleteView.as_view(), name='product-delete'),
    # Add other URL patterns as needed
]

