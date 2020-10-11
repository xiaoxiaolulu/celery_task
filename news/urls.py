from django.urls import path

from news import views

app_name = 'news'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('welcome/', views.welcome, name='welcome'),
    path('category/', views.category_list, name='category'),
    path('new/', views.new_list, name='new')
]
