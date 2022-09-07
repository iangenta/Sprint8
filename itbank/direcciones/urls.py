from django.urls import path
from .views import DireccionF

urlpatterns = [
    path('<int:pk>/',DireccionF.as_view()),
    #path('', AuthUserList.as_view(), name= 'API'), 
     ]