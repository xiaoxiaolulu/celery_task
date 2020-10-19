from django.urls import path

from task_config import views

app_name = 'task_config'

urlpatterns = [
    path('config_list/', views.config_list, name='config_list'),
    path('tasks_queue_conf_list/', views.task_queue_conf_list, name='tasks_queue_conf_list'),
]
