from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
# Create your views here.
#create a bookfilter

class BookFilter(filters.FilterSet):
    minimum_publication_year = filters.DateFilter(field_name='publication_year',lookup_expr='gte')
    maximum_publication_year = filters.DateFilter(field_name='publication_year',lookup_expr = 'lte')
    class Meta:
        model = Book
        fields = ['minimum_publication_year','maximum_publication_year','author__name']
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = ['title','author']
    # ordering = ['publication_year']
#create a filterset that uses the bookfilter
#DjangoFilterBackend
#select_related
class SelectRelated(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['author']
    # ordering = ['author']