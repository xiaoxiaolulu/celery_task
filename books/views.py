from django.shortcuts import render


# Create your views here.
def book_list(request):
    return render(request, 'task_push_list.html')


def to_add_book(request):

    return render(request, 'book_add.html')


