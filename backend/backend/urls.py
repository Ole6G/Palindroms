"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from books.views import BooksPublishedAfterDateView, AuthorWithMostBooksView, AuthorRevenueView, \
    BooksContainingPythonView, BooksListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books23+/', BooksPublishedAfterDateView.as_view(), name='books_list'),
    path('most-books-author/', AuthorWithMostBooksView.as_view(), name='most_books_author'),
    path('author-revenue/', AuthorRevenueView.as_view(), name='author_revenue'),
    path('containing-python/', BooksContainingPythonView.as_view(), name='books_containing_python'),
    path('list-books/', BooksListView.as_view(), name='books_list'),

]
