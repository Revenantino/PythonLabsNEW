from django.contrib import admin
from .models import Medicine


# Модель товара
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available_quantity', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available_quantity', 'available']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Medicine, MedicineAdmin)