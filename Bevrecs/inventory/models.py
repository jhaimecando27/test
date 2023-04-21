from django.db import models


STOCK_CATEGORY = (
    # Left, For database para hindi mahaba masyado. Tas trip ko
    # Right, For user interface
    ("INGRI", "Ingridients"),
    ("AO", "Add-Ons"),
    ("UT", "Utensils"),
)


class Stocks(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(choices=STOCK_CATEGORY, max_length=10)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    date_in = models.DateField()
    expiration = models.DateField()

    def __str__(self):
        return self.name
