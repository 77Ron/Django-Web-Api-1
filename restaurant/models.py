from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


DELIVERY_STATUS_CHOICES = (
    ('pending', 'PENDING'),
    ('failed', 'FAILED'),
    ('completed', 'COMPLETED')
)

# Create your models here.
class Meal(models.Model):
    # Name of the meal.
    name = models.CharField("Name of the Meal", max_length=100)
    # Description of the meal.
    description = models.TextField("Description of the Meal", blank=True, null=True)
    # Store the meal price.
    price = models.DecimalField("Price (£)", max_digits=10, decimal_places=2)
    # Images of the meals.
    image = models.ImageField(upload_to='meal_images', default='meal_images/default_meal.jpg')
    # Availability of the meal.
    available = models.BooleanField("Online Availability", default=False)
    # Stock count.
    stock = models.IntegerField("Stock Count", default=0)

    def __str__(self):
        return f'{self.description}'
    
class OrderTransaction(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField('Amount Paid (£)', max_digits=64, decimal_places=2, default=0)
    status = models.CharField('Delivery Status', max_length=9, choices=DELIVERY_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField('Date Created', default=now)
