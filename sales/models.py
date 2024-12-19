from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales")
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"