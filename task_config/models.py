from django.db import models


class ScheduleConf(models.Model):

    id = models.AutoField(primary_key=True)
    queue_name = models.CharField(max_length=64)
    routing_content = models.CharField(max_length=64)

    class Meta:
        db_table = 'schedule_conf'


class ScheduleCronConf(models.Model):

    id = models.AutoField(primary_key=True)
    schedule_name = models.CharField(max_length=64)
    task_name = models.CharField(max_length=64)
    task_path = models.CharField(max_length=255)
    task_hour = models.IntegerField()
    task_minute = models.IntegerField()
    schedule_queue = models.CharField(max_length=64)
    queue_id = models.ForeignKey('ScheduleConf', models.DO_NOTHING, null=True, db_column='queue_id', blank=True)

    class Meta:
        db_table = 'schedule_cron_conf'
