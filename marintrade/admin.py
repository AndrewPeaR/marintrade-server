from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Company, CompanyTags

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "company")

@admin.register(CompanyTags)
class CompanyTagsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "official_site", "get_tags", "preview")
    # Автоматизация заполнения слага
    prepopulated_fields = {'slug': ('name',)}
    # Показ всех тегов
    def get_tags(self, obj):
        return ", ".join([tag.title for tag in obj.company_tag.all()])
    get_tags.short_description = 'Тэги компании'
    # Предпросмотр картинки элемента
    readonly_fields = ["preview"]
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;">')