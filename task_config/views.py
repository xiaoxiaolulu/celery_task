from django.shortcuts import render


# Create your views here.
def config_list(request):
    return render(request, 'tasks_config_list.html')
