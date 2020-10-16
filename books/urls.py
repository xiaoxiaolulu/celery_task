from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('book/', views.book_list, name='book'),
    path('to_add_book/', views.to_add_book, name='to_add_book')
]
