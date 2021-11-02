from django.db import models
from authentication.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class WomenProduct(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    image_1 = models.ImageField(upload_to='women_product', help_text='Women product image', blank=False)
    image_2 = models.ImageField(upload_to='women_product', help_text='Women product image', blank=True)
    image_3 = models.ImageField(upload_to='women_product', help_text='Women product image', blank=True)
    image_4 = models.ImageField(upload_to='women_product', help_text='Women product image', blank=True)
    image_5 = models.ImageField(upload_to='women_product', help_text='Women product image', blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    new = models.BooleanField(default=True)
    kind = models.CharField(max_length=10, default='jacket, pants, t-short, sweatshirt, dress, shoes', blank=False)
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

