#  Habibullah
#  @ Dragunov
#  Unixian@outlook.com  
#  4/12/2016

from django.http import HttpResponse ,Http404
from django.shortcuts import get_object_or_404

from django.views import generic
from .models import Product

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'Products/index.html'
    context_object_name = 'All_Products'
    def get_queryset(self):
        return Product.objects.all()


# instead of function we use classes
# class IndexView(generic.ListView)
# 	template_name='Products/index.html'
# 	def get_queryset(self):
# 		return Album.objects.all()

# class DetailView(generic.DetailView)
# 	model = Album
# 	template_name='Products/detail.html'

# views.IndexView.as_view()

# ListView :::: object_list
# context_object_name = 'Any name '



# def index(Request) :
#     All_Products = Product.objects.all()
#     # render(Request,Template, Dictionary)
#     return render(Request, 'Products/index.html', {'All_Products' : All_Products})

# def detail (Request, Product_ID) :
#     try:
#         Product_Requested = Product.objects.get(pk=Product_ID)
#     except Product.DoesNotExist:
#         raise Http404("Page Does not Exist")
#     # Product = get_object_or_404(Product, pk=Album_ID)

#     return render(Request, 'Products/ProductView.html',{'Product_Requested' : Product_Requested})

class DetailView(generic.DetailView):
    model = Product
    context_object_name = 'One_Album'
    template_name = 'Products/detail.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'Products/signup_form.html'

    # display blank form 
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})
    
    # Process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Authentcation
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Products:index')
        # If something went wrong            
        return render(request, self.template_name,{'form':form})