from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
    path('category/<slug:category_slug>/', views.CategoryView.as_view(), name='category_filter'),
]
