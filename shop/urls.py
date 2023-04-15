from . import views
from django.urls import path


urlpatterns = [
    path('', views.VehicleView.as_view(), name="home"),
    path('<str:id>/', views.VehicleDetail.as_view(), name='vehicle_detail')
]