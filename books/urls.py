from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('book_list/', views.BookListView.as_view(),name='book_list'),
    path('to_add_book/', views.to_add_book, name='to_add_book'),
    path('add_book/', views.add_book, name='add_book')
]
