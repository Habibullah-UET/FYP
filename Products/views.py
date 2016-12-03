#  Habibullah
#  @ Dragunov
#  Unixian@outlook.com  
#  4/12/2016

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product

def index(Request) :
    All_Products = Product.objects.all()
    # render(Request,Template, Dictionary)
    return render(Request, 'Products/index.html', {'All_Products' : All_Products})

def detail (Request, Product_ID) :
    try:
        Product_Requested = Product.objects.get(pk=Product_ID)
    except Product.DoesNotExist:
        raise Http404("Page Does not Exist")
    # Product = get_object_or_404(Product, pk=Album_ID)

    return render(Request, 'Products/ProductView.html',{'Product_Requested' : Product_Requested})

