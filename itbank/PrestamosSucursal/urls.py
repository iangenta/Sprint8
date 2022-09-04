from django.urls import path
from .views import PrestamoList

urlpatterns = [
    path('<int:branch_id>/',PrestamoList.as_view()),
     ]