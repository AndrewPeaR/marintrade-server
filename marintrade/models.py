from django.db import models
# from django.conf import settings
# from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Company(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    official_site = models.TextField()
    company_tag = models.TextField()
    slug = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name
