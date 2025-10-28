from django.db import models

class Customer(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0)

  def __str__(self):
    return self.name
  
class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=8, decimal_places=2)

  def __str__(self):
    return self.name
  
class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  total_price = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Ordine #{self.id} - {self.customer.name}"
