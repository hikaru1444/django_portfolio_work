from django.db import models

# Create your models here.


class Works(models.Model):
    name = models.CharField('名前', max_length=100)
    date = models.DateField('日付')
    in_time = models.TimeField('出勤')
    out_time = models.TimeField('退勤')
    rest_time = models.TimeField('休憩', default='00:00')
    other = models.CharField('備考', max_length=1000, default='', blank=True)

    def __str__(self):
        return self.name
