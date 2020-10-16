from books.models import Book, BookPush, BookPushLog
from celery import task, platforms

platforms.C_FORCE_ROOT = True


@task
def push_book():
    book = Book.objects.order_by('count').first()
    BookPush.objects.all().delete()
    push = BookPush(book_id=book)
    push.save()
    log = BookPushLog(book_id=book)
    log.save()
    return 'success'
