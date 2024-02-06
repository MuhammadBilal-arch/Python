# views.py
from rest_framework import generics
from .models import Cat
from .serializers import CatSerializer

class CatListCreate(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class CatRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer