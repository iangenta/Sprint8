from django.urls import path
from .views import PrestamoLists


urlpatterns = [
    path('',PrestamoLists.as_view())
     ]