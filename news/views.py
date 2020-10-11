from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'index.html')


def category_list(request):
    return render(request, 'news_category_list.html')


def new_list(request):
    return render(request, 'news_new_list.html')


def welcome(request):
    return render(request, 'welcome.html')
