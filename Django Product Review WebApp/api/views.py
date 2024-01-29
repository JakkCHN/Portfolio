from django.shortcuts import render
from rest_framework. viewsets import ModelViewSet
from itreporting.models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
permission_classes = [IsAuthenticatedOrReadOnly]
# Create your views here.

class ProductViewSet(ModelViewSet):
    
    queryset = Product.objects.all().order_by('date_submitted')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)