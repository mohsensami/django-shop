from django.shortcuts import render
from django.views import View
from .models import Product



class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shop/home.html', {'products': products})


class DetailView(View):
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        return render(request, 'shop/detail.html', {'product': product})