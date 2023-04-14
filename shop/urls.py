from . import views
from django.urls import path


urlpatterns = [
    path('', views.VehicleView.as_view(), name="home")
]