from django.urls import path
from .views import PrestamoLists


urlpatterns = [
    path('<int:pk>/',PrestamoLists.as_view())
     ]