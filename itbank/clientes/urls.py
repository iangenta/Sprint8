from django.urls import path
from .views import ClienteDetails

urlpatterns = [
    path('<int:pk>/',ClienteDetails.as_view()),
    #path('', AuthUserList.as_view(), name= 'API'), 
     ]