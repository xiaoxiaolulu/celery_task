from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('book/', views.book_list, name='book'),
]
