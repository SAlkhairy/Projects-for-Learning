# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from django.http import Http404

from.models import Article

# Create your views here.

#def home(request):
    #return HttpResponse('This is the homepage')

def index(request):
    return HttpResponse('Hello from the news app index view!')

def list(request):
    list = Article.objects.order_by('-pub_date')[:5]
    context = {'list':list}
    return render(request, 'newsapp/list.html', context )

def show(request, article_id):
    # try:
    #     article = Article.objects.get(pk= article_id)
    # except Article.DoesNotExist:
    #     raise Http404('Sorry, this page does not exist.')
    # return render(request, 'newsapp/show.html', {'article':article} )

    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'newsapp/show.html', {'article': article} )


