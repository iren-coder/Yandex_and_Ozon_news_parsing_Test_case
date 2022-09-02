from django.db import models
from datetime import date, datetime
from django.utils import timezone

# Create your models here.

class News(models.Model):
    title = models.TextField(null=True, blank=True)
    date = models.DateField(null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    tag = models.TextField(null=True, blank=True)
    NEWS_CANAL = [
		('Y','yandex'),
		('O','ozon'),
    ]
    canal = models.CharField(max_length=2, choices=NEWS_CANAL, default='Y')
    def __str__(self):
        return f'{self.id}'


