from datetime import datetime
from django.db import models


class Book(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    content = models.CharField(max_length=255)
    c_time = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'book'


class BookPush(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey('Book', models.DO_NOTHING, blank=True, null=True, db_column='book_id')
    p_time = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'book_push'


class BookPushLog(models.Model):

    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey('Book', models.DO_NOTHING, blank=True, null=True, db_column='book_id')
    p_time = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'book_push_log'
