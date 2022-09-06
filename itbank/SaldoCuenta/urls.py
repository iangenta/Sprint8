from django.urls import path
from .views import SaldoCuenta

urlpatterns = [
    path('',SaldoCuenta.as_view()),
     ]