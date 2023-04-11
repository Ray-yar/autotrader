from django.contrib import admin
from .models import Vehicle
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Vehicle)
class VehicleAdmin(SummernoteModelAdmin):
    
    list_filter = ('status', 'make', 'created_at')
    search_fields = ['make', 'model', 'year', 'body', 'fuel']
    list_display = ('make', 'model', 'year', 'body', 'fuel', 'status', 'approved', 'created_at')
    summernote_fields = ('content')
    actions = ['approve_vehicle']

    def approve_vehicle(self, request, queryset):
        queryset.update(approved=True)
        queryset.update(status=1)