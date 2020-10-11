from django.urls import path

from task_config import views

app_name = 'task_config'

urlpatterns = [
    path('config/', views.config_list, name='config'),
]
