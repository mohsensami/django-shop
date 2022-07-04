from django.urls import path
from . import views


app = 'orsers'
urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart')
]
