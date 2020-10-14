from datetime import datetime
from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=255)
    c_time = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'news_category'


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=64)
    new_time = models.CharField(max_length=32)
    excel_dir = models.FileField(upload_to='excle_files/', max_length=255, blank=True, null=True)
    category_id = models.ForeignKey('NewsCategory', models.DO_NOTHING, blank=True, null=True, db_column='category_id')

    class Meta:
        db_table = 'news_new'
