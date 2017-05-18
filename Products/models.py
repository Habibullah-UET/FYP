#  Habibullah
#  @ Dragunov
#  Unixian@outlook.com  
#  08/05/2017

from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem

class ShoppingWebsite(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Product(models.Model):
    Title = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=200)
    price =  models.CharField(max_length=10)
    Rating = models.CharField(max_length=3)
    Reviews = models.TextField()
    Website = models.ForeignKey(ShoppingWebsite)
    url = models.URLField()
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Title


class ProductItem(DjangoItem):
    django_model = Product
