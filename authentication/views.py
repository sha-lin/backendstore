from django.shortcuts import render
from rest_framework import generics, status, views, permissions

# Create your views here.

class RegisterView(generics.GenericAPIView):
    def post(self, request):
        user = request.data
