from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Article

def index(request):
    article_list = Article.objects.order_by('-pub_date')[:5]
    year_list = []
    for i in article_list:
        year_list.append(i.pub_date.year)
    year_list = list(set(year_list))
    context = {'year_list': year_list}
    return render(request, 'news/base.html', context)

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def article_detail(request, headline):
    art = get_object_or_404(Article, headline=headline)
    return render(request, 'news/detail.html', {'article':art,})