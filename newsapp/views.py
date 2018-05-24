# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Article, Comment

def index(request):
    return HttpResponse('Hello from the news app index view!')

def list(request):
    list = Article.objects.order_by('-pub_date')[:5]
    context = {'list':list}
    return render(request, 'newsapp/list.html', context )

def show(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'newsapp/show.html', {'article': article} )

def comment(request, article_id):
    text = request.POST['text']
    author = request.POST['author']
    article = get_object_or_404(Article, pk=article_id)

    Comment.objects.create(text=text, author=author, article=article)
    redirect_url = reverse('newsapp:show', args=[article_id])
    return HttpResponseRedirect(redirect_url)
