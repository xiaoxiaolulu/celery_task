from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from books.models import Book


def to_add_book(request):
    from .tasks import push_book
    push_book()
    return render(request, 'book_add.html')


def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        book = Book(name=name, content=content)
        book.save()
        return JsonResponse({"code": 200, "msg": "success"})


class BookListView(ListView):
    model = Book
    template_name = 'task_push_list.html'
    context_object_name = 'books'
    paginate_by = 10
    ordering = 'id'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(*kwargs)
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
        count = Book.objects.all().count()

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': num_pages,
            'count': count,
        }
