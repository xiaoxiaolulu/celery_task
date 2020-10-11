from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from news.models import NewsCategory


def main(request):
    return render(request, 'index.html')


def category_list(request):
    return render(request, 'news_category_list.html')


def new_list(request):
    return render(request, 'news_new_list.html')


def welcome(request):
    return render(request, 'welcome.html')


def add_category(request):

    if request.method == 'GET':
        return render(request, 'news_category_add.html')

    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category_desc = request.POST.get("category_desc")
        new_category = NewsCategory(name=category_name, desc=category_desc)
        new_category.save()
        return JsonResponse({"code": 200, "msg": "添加成功"})


def add_news(request):

    if request.method == 'GET':
        return render(request, 'news_new_add.html')

    if request.method == 'POST':
        return JsonResponse({"code": 200, "msg": "导入数据成功"})
