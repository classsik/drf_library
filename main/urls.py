from django.urls import path
from .views import *


urlpatterns = [
    path('books', get_books),
    path('books/<int:pk>', get_book),
    path('books/create', create_book),
    path('books/edit/<int:pk>', edit_book),
    path('books/delete/<int:pk>', delete_book),
]
