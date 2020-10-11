from django.shortcuts import render


# Create your views here.
def book_list(request):
    return render(request, 'task_push_list.html')
