import html
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
    reg_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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

    # def __str__(self):
    #     return html.escape(self.content)
        


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vcl = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='reviews', default=1)
    title = models.CharField(max_length=100)
    text = models.TextField()
    approved = models.BooleanField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
