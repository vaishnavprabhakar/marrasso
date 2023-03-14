from django.db import models

# Create your models here.

class CustomUser(models.Model):
    username = models.TextField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=200)
    

    def __str__(self):
        return self.username


# class Products(models.Model):
    
#     product_name = models.CharField(max_length=150)
#     projduct_desc = models.CharField(max_length=200)
#     product_price  = models.FloatField()
#     product_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

