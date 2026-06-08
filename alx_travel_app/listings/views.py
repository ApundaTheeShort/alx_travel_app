from django.shortcuts import render
from .models import Listing
from .serializers import ListingSerializer
from rest_framework import generics

# Create your views here.


class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
