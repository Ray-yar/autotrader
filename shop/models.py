from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
# Create your models here.
class Vehicle(models.Model):
    make = models.CharField(max_length=128, blank=False)
    model = models.CharField(max_length=128, blank=False)
    color = models.CharField(max_length=128, blank=False)
    body = models.CharField(max_length=128, blank=False)
    year = models.IntegerField()
    fuel = models.CharField(max_length=128)
    milage = models.IntegerField()
    reg_price = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    featured_photo = CloudinaryField('image', default='placeholder')
    transmission = models.CharField(max_length=128)
    content = models.TextField(default="No Details")
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"