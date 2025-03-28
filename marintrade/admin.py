from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Company

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "company")
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "official_site", "preview")
    # Предпросмотр картинки элемента
    readonly_fields = ["preview"]
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;">')