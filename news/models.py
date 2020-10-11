from datetime import datetime
from django.db import models


# Create your models here.
class NewsCategory(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=255)
    c_time = models.DateTimeField(default=datetime.now())

    class Meta:

        db_table = 'news_category'


class News(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=64)
    new_time = models.CharField(max_length=32)
    category_id = models.ForeignKey('NewsCategory', models.DO_NOTHING, db_column='category_id', blank=True, null=True)
    c_time = models.DateTimeField(default=datetime.now())

    class Meta:

        db_table = 'news_new'
