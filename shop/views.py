from django.shortcuts import render
from django.views import View
from .models import Product, Category


class HomeView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.all()
        categories = Category.objects.filter(is_sub=False)
        return render(request, 'shop/home.html', {'products':products, 'categories':categories})


class DetailView(View):
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        return render(request, 'shop/detail.html', {'product': product})


class CategoryView(View):
    def get(self, request, category_slug):

        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)
        return render(request, 'shop/category.html', {'products': products})