from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_picture = models.ImageField(upload_to='product_pictures/', blank=True, null=True)
    manufacturer = models.CharField(max_length=255)
    average_cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()
    ratings = models.IntegerField(default=0)
    date_submitted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} Item: {self.manufacturer}'
    def get_absolute_url(self):
        return reverse('itreporting:issue-detail', kwargs = {'pk': self.pk})
