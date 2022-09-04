from django.urls import path
from .views import TarjetasList

urlpatterns = [
    path('<int:customer_id>/',TarjetasList.as_view()),
    #path('', AuthUserList.as_view(), name= 'API'), 
     ]