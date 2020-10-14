import os
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from celery_task.settings import BASE_DIR
from news.models import NewsCategory, News
from news.tasks import data_new


def main(request):
    return render(request, 'index.html')


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
        file = request.FILES.get('exc_file')
        stream = open(os.path.join(BASE_DIR, 'medias', 'excel_files', file.name), 'wb')
        for chunk in file.chunks():
            stream.write(chunk)
        stream.close()
        df = pd.read_excel(f"{BASE_DIR}/medias/excel_files/{file.name}")

        data_new.delay(df)
        return JsonResponse({"code": 200, "msg": "导入数据成功"})


class CategoryListView(ListView):
    model = NewsCategory
    template_name = 'news_category_list.html'
    context_object_name = 'newsCategorys'
    paginate_by = 10
    ordering = 'c_time'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(*kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj, 3)
        context.update(pagination_data)
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = False

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page - around_count, current_page)

        if current_page >= num_pages - around_count - 1:
            right_pages = range(current_page + 1, num_pages + 1)
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + around_count + 1)

        # 查询总条数
        count = NewsCategory.objects.all().count()

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': num_pages,
            'count': count,
        }


class NewListView(ListView):
    model = News
    template_name = 'news_new_list.html'
    context_object_name = 'news'
    paginate_by = 10
    ordering = 'id'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(NewListView, self).get_context_data(*kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj, 3)
        context.update(pagination_data)
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = False

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page - around_count, current_page)

        if current_page >= num_pages - around_count - 1:
            right_pages = range(current_page + 1, num_pages + 1)
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + around_count + 1)

        # 查询总条数
        count = News.objects.all().count()

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': num_pages,
            'count': count,
        }
