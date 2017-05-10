#  Habibullah
#  @ Dragunov
#  4/12/2016

from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
app_name = 'Products'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = "index"),
    url(r'^register/$', views.UserFormView.as_view(), name = "register"),
    url(r'^accounts/profile/$', views.IndexView.as_view(), name = "login"),
    url(r'^login/$', auth_views.login, {'template_name': 'Products/Login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'Products/index.html'}, name='logout'),
    url(r'^(?P<Product_ID>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
]


