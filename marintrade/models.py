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

class Product(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Test(models.Model):
    title = models.CharField(max_length=200)
    exerpt = models.TextField(max_length=200)
    content = HTMLField()

    def __str__(self):
        return self.title
