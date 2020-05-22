from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/', views.year_archive, name='year'),
    path('<headline>/', views.article_detail, name='headline'),
]
