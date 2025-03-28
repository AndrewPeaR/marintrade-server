from django.db import models
from django.core.validators import FileExtensionValidator
# from django.conf import settings
# from django.utils import timezone

class Company(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    official_site = models.TextField()
    company_tag = models.TextField()
    slug = models.TextField()
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