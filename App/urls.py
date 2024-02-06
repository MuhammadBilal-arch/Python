# urls.py
from django.urls import  path
from .views import CatListCreate, CatRetrieveUpdateDestroy

urlpatterns = [
    path('cats/', CatListCreate.as_view()),
    path('cats/<int:pk>/', CatRetrieveUpdateDestroy.as_view()),
]