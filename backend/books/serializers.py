from rest_framework import serializers
from .models import Author, Book, BookSale


class AuthorSerializer(serializers.ModelSerializer):
    revenue = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'revenue']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSale
        fields = '__all__'
