from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Company, CompanyTags, ProductsBlock, Portfolio

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "link", "preview")
    
    readonly_fields = ["preview"]
    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;">')
        else:
            return 'No file'

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

@admin.register(ProductsBlock)
class ProductsBlockAdmin(admin.ModelAdmin):
    list_display = ("title",'description', 'get_products', 'company')

    def company(self, obj):
        return obj.company.name
    
    def get_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
    get_products.short_description = 'Товары'
    
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'preview', 'pdf')
    
    readonly_fields = ["preview"]
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;">')