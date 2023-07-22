from . import views
from django.urls import path


urlpatterns = [
    path('', views.VehicleView.as_view(), name="home"),
    path('<str:id>/', views.VehicleDetail.as_view(), name='vehicle_detail'),
    path('review/<int:id>/delete/', views.VehicleDetail.as_view(), name='review-delete'),
    path('review/<int:id>/edit/', views.VehicleDetail.as_view(), name='review-edit'),
]