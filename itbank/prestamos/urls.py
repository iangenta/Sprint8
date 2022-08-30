from django.urls import path
from .views import PrestamoDetails

urlpatterns = [
    path('',PrestamoDetails.as_view()),
    #path('', AuthUserList.as_view(), name= 'API'), 
     ]