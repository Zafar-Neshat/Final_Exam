from msilib.schema import ListView
from django.shortcuts import render
from app.exam.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'