from dataclasses import field, fields
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Nutrition, Product
from .forms import ProductForm
# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('products')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('products')
            else:
                messages.info(request, 'Username OR password is incorrect!')

        context = {}
        return render(request, 'products/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login_user')

class ProductsView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

class UserDashboardTemplateView(TemplateView):
    # I want to insert the ORDER model in this class also
    model = Product
    context_object_name = "products"
    template_name = "products/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()  # or whatever
        context['nutritions'] = Nutrition.objects.all()  # or whatever
        return context
    
    @method_decorator(login_required(login_url="/login"))
    def dispatch(self, *args, **kwargs):
        return super(UserDashboardTemplateView, self).dispatch(*args, **kwargs)

@login_required(login_url='/login')
def createProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
    context = {'form':form}
    return render(request, 'products/product_form.html', context)

@login_required(login_url='login_user')
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products')

    context = {'form':form}
    return render(request, 'products/product_form.html', context)

@login_required(login_url='login_user')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/products')
    context = {'product': product}
    return render(request, 'products/delete.html', context)

# @login_required(login_url='login_user')
# def products(request):
#     return render(request, 'products/products.html')

@login_required(login_url='login_user')
def nutrition(request):
    return render(request, 'products/nutrition.html')