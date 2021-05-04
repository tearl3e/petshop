from django.db import models
from PIL import Image
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', verbose_name='Image', default='default.jpg')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.id])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100, null=True)
    animal = models.CharField(max_length=50, default='Empty')
    image = models.ImageField(upload_to='images/', verbose_name='Image', default='default.jpg')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])
