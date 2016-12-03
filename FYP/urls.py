#  Habibullah
#  @ Dragunov
#  4/12/2016

from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Products/',include('Products.urls')),
]
