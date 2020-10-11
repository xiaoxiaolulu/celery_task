from django.urls import path

from news import views

app_name = 'news'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('welcome/', views.welcome, name='welcome'),
    path('category/', views.category_list, name='category'),
    path('add_category/', views.add_category, name='add_category'),
    path('new/', views.new_list, name='new'),
    path('add_new/', views.add_news, name='add_new')
]
