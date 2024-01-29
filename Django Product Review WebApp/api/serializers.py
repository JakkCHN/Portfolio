# api/serializers.py
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from itreporting.models import Product  # Add 'Product' to the imports

class ProductSerializer(ModelSerializer):  # Add the ProductSerializer class
    # Define the necessary fields for Product serialization
    class Meta:
        model = Product
        fields = ['name', 'product_picture', 'manufacturer', 'average_cost', 'category', 'release_date', 'description', 'ratings']
