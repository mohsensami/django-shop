from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('verify/', views.UserRegisterVerifyCodeView.as_view(), name='verify_code'),
]
