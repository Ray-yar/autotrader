from django.contrib import admin
from .models import Vehicle, Review, Contact
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


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    
    list_filter = ('title',)
    search_fields = ['title',]
    list_display = ('title', 'approved')
    summernote_fields = ('text')
    actions = ['approve_review']

    def approve_review(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    
    list_filter = ('subject',)
    search_fields = ['subject',]
    list_display = ('subject',)
    summernote_fields = ('text')