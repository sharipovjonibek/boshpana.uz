from django.contrib import admin
from .models import Rental, RentalImage, Listing

class RentalImageInline(admin.TabularInline):
    model = RentalImage
    extra = 1

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['title', 'city', 'district', 'price', 'rooms', 'verified', 'is_active', 'created_at']
    list_filter = ['city', 'property_type', 'verified', 'is_active', 'created_at']
    search_fields = ['title', 'description', 'address']
    list_editable = ['verified', 'is_active']
    inlines = [RentalImageInline]
    
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description', 'property_type', 'owner')
        }),
        ('Joylashuv', {
            'fields': ('city', 'district', 'address')
        }),
        ('Texnik ma\'lumotlar', {
            'fields': ('price', 'rooms', 'area', 'floor', 'total_floors')
        }),
        ('Qulayliklar', {
            'fields': ('has_balcony', 'has_parking', 'has_elevator', 'has_air_conditioning', 'has_internet', 'has_furniture')
        }),
        ('Status', {
            'fields': ('verified', 'is_active')
        }),
    )

@admin.register(RentalImage)
class RentalImageAdmin(admin.ModelAdmin):
    list_display = ['rental', 'image', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']
    search_fields = ['rental__title']

admin.site.register(Listing)
