from django.shortcuts import render
import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import permissions
from rest_framework import generics,filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from rest_framework.filters import SearchFilter
from datetime import datetime, timedelta
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Register
from .serializer import Register_serilizer
from .models import Post,Comment
from .serializer import Comment_serilizer,Post_serilizer


# ___________________ register________

class Register_list(ListCreateAPIView):
    queryset=Register.objects.all()
    serializer_class=Register_serilizer
    permission_classes=[permissions.AllowAny]

# _______________________ Blog APi_______________________
class postlist(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=Post_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class postdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=Post_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]
class comment_view(generics.CreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=Comment_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
