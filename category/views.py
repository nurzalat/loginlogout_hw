from django.shortcuts import render
from rest_framework import generics

from category import serializers
from category.models import Category


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer