from django.shortcuts import render
from apps.products.models import Product

def home_page(request):
    products = Product.objects.all().order_by('created_at')
    return render(request, "home/home.html", {'products': products})


def about_page(request):
    return render(request, "home/about.html")

