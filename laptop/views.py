from django.db.models import query
from rest_framework import generics, serializers
from rest_framework import permissions
from rest_framework import authentication
from .serializers import LaptopAllSeriaLizers
from .models import Laptop
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render




class LaptopCreateView(generics.CreateAPIView):
    serializer_class = LaptopAllSeriaLizers
    permissions_classes = LaptopAllSeriaLizers
    permissions_classes = (IsAuthenticated,IsAdminUser)

class LaptopListView(generics.ListAPIView):
    serializer_class = LaptopAllSeriaLizers
    queryset = Laptop.objects.all()

class LaptopDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LaptopAllSeriaLizers
    queryset = Laptop.objects.all()
    permissions_classes = (IsOwnerOrReadOnly,IsAuthenticated)
    authentication_classes = (TokenAuthentication,SessionAuthentication)




def oauth(request):
    return render(request,'oauth.html')