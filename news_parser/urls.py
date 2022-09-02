from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from news_parser import views
from rest_framework import routers
from news_parser.views import News
from news_parser.views import NewsDetail
from news_parser.views import NewsListFilter

router = routers.DefaultRouter()
router.register(r'newslist', views.NewsListFilter, basename = 'news-list')

urlpatterns = [
    path('', include(router.urls)),
    path('newslist/<int:pk>', NewsDetail.as_view(), name='news-detail'),
]