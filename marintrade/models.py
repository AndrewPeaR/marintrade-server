from django.db import models
from django.core.validators import FileExtensionValidator

from tinymce.models import HTMLField
# from django.conf import settings
# from django.utils import timezone

class CompanyTags(models.Model):
    title = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Тэги вендоров"

    def __str__(self):
        return self.title

class Company(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    official_site = models.TextField(verbose_name='Официальный сайт')
    company_tag = models.ManyToManyField(CompanyTags)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='companies', verbose_name='Логотип компании', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name_plural = "Вендоры"

    def __str__(self):
        return self.name
    
class ProductsBlock(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='Компания')    
    
    class Meta:
        verbose_name_plural = "Блоки с товарами"

    def __str__(self):
        return self.title
    
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(upload_to='products', verbose_name='Логотип компании', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))], null=True, blank=True)
    link = models.CharField(max_length=300, verbose_name='Ссылка при нажатии', null=True, blank=True)
    productsBlock = models.ForeignKey(ProductsBlock, blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
    
def path_portfolio(instance, filename):
    return '/'.join(filter(None, ('portfolio', instance.title, filename)))

class Portfolio(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(upload_to=path_portfolio, verbose_name='Изображение', null=True, blank=True)
    pdf = models.FileField(upload_to=path_portfolio, verbose_name='Документ', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Портфолио"

    def __str__(self):
        return self.title

class Questions(models.Model):
    name = models.CharField(max_length=65, verbose_name='Имя')
    phoneNumber = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.CharField(max_length=50, verbose_name='E-mail')
    question = models.TextField(verbose_name='Вопрос')
    status = models.BooleanField(verbose_name='Обработан', default=False)
    create_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обработки', auto_now=True)

    class Meta:
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.name