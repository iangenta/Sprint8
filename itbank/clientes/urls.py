from django.urls import path
from . import views
from .views import ClienteDetails,index_clientes
urlpatterns = [
    path('api/',ClienteDetails.as_view()),
    path('',views.index_clientes, name='index_clientes'),
    #path('', AuthUserList.as_view(), name= 'API'), 
     ]