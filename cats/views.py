from rest_framework import generics

from .models import Cat
from .serializers import CatSerializer
from rest_framework import viewsets


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
# class CatList(generics.ListAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer
#
#
# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer
