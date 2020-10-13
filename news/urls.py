from django.urls import path

from news import views

app_name = 'news'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('welcome/', views.welcome, name='welcome'),
    path('category_list/', views.CategoryListView.as_view(), name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('new_list/', views.NewListView.as_view(), name='new_list'),
    path('add_new/', views.add_news, name='add_new')
]
