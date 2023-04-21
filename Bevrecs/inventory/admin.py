from django.contrib import admin

# Register your models here.
from .models import Stocks


class StocksAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "quantity", "price", "date_in", "expiration")


admin.site.register(Stocks, StocksAdmin)
