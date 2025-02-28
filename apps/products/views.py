from django.shortcuts import render
from .models import Product

def products(request):
    products = Product.objects.all().order_by('created_at')
    return render(request, 'products/products.html', {'products': products})
    
