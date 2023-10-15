from django.shortcuts import render
from . models import ProductModel


def home(request):
    products = ProductModel.objects.all()

    return render(request, 'base/home.html', {'products':products})