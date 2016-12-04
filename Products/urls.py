#  Habibullah
#  @ Dragunov
#  4/12/2016

from django.conf.urls import url, include
from . import views
app_name = 'Products'

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^(?P<Product_ID>[0-9]+)/$', views.detail, name="detail"),
]
