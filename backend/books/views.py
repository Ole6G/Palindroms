from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Sum, F
from .models import Book, Author, BookSale
from .serializers import BookSerializer, AuthorSerializer


class BooksListView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


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


class AuthorRevenueView(APIView):
    def get(self, request, *args, **kwargs):
        authors = Author.objects.annotate(
            revenue=Sum(F('book__price') * F('book__booksale__quantity'))
        )
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


class BooksContainingPythonView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.filter(title__icontains="Python")
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
