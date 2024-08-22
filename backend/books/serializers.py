from rest_framework import serializers
from .models import Author, Book, BookSale


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSale
        fields = '__all__'
