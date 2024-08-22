from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BooksPublishedAfterDateView(APIView):
    def get(self, request, *args, **kwargs):
        date = "2023-01-01"
        books = Book.objects.filter(publication_date__gt=date, price__lt=30, is_available=True)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class AuthorWithMostBooksView(APIView):
    def get(self, request, *args, **kwargs):
        most_books_author = Author.objects.annotate(num_books=Count('book')).order_by('-num_books').first()
        serializer = AuthorSerializer(most_books_author)
        return Response(serializer.data)
