from django.contrib import admin
from .models import Author, Book, BookSale
from datetime import date
from django.db.models import Count, Sum, F


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'price', 'is_available')


# Кастомизация админ-панели для модели Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


# Регистрация модели BookSale, если она еще не зарегистрирована
@admin.register(BookSale)
class BookSaleAdmin(admin.ModelAdmin):
    list_display = ('book', 'quantity', 'sale_date')
