from django.template import loader
from django.http import HttpResponse
#from django.shortcuts import redirect, render
#from django.urls.base import reverse_lazy
#from django.views.generic.list import ListView
#from rest_framework.parsers import JSONParser
from .models import News
from .serializers import *
from rest_framework import generics  
from django.core import serializers
#from django.core.exceptions import ValidationError, ObjectDoesNotExist
#from json import JSONDecodeError
from django_filters import rest_framework as filters
#from django.db import IntegrityError
#from rest_framework.response import Response
from rest_framework.views import APIView
#from types import SimpleNamespace
#from django.db.models import Q
from rest_framework.generics import ListAPIView
from django.views.generic import ListView, CreateView, UpdateView, View
#mport gc
from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import mixins
#from rest_framework.mixins import ListModelMixin
from rest_framework import viewsets
#from rest_framework.decorators import action
from rest_framework import filters
# Create your views here.

# Класс для фильтрации элементов в списке
# Фильтрация осуществляется по дате, тэгу, каналу (Яндекс или Озон)

# Для фильтрации новости по дате пользуйтесь кнопкой Filters REST-интерфейса либо вбейте в строке браузера
# http://localhost/api/v1/newslist/?search=date
# например, чтобы получить все новости за 25 августа:
# http://localhost/api/v1/newslist/?search=2022-08-25

# Для фильтрации новости по тэгу пользуйтесь кнопкой Filters REST-интерфейса либо вбейте в строке браузера
# http://localhost/api/v1/newslist/?search=tag
# например, чтобы получить все новости с тэгом FBS:
# http://localhost/api/v1/newslist/?search=fbs

# Для фильтрации новости по источнику новости (Яндекс canal=y, OZON canal=o) пользуйтесь кнопкой Filters REST-интерфейса 
# либо вбейте в строке браузера
# http://localhost/api/v1/newslist/?search=canal
# например, чтобы получить все новости от OZON:
# http://localhost/api/v1/newslist/?search=o

class NewsListFilter(viewsets.ModelViewSet):
    
    queryset = News.objects.all()
    serializer_class = NewsSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] 
    search_fields = ['date', 'canal', 'tag']

# Класс для детализации новости по её id
class NewsDetail(generics.RetrieveAPIView):  
    queryset = News.objects.all()  
    serializer_class = NewsSerializer

# Все роуты проекта:
def links(request):
    template = loader.get_template('links.html')
    data = {
        "title": "Все роуты проекта",
    }
    return HttpResponse(template.render(data, request))
