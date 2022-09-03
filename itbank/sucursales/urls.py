from django.urls import path
from .views import SucursalList

urlpatterns = [
    path('',SucursalList.as_view()),
     ]