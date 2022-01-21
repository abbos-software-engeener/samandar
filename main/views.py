from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from main.models import Book
from main.serializer import BookSerializer


class View( RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailView(CreateAPIView,ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer