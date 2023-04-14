from django.shortcuts import render
from django.views import generic
from .models import Vehicle

# Create your views here.
class VehicleView(generic.ListView):
    model = Vehicle
    object = Vehicle.objects.filter(status=1).order_by('created_at')
    template_name = "index.html"
    paginate_by = 6

