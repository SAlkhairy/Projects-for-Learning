# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=80)
    title = models.CharField(max_length=200, default='First Title')
    body = models.TextField(max_length=500)
    image = models.ImageField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    article = models.ForeignKey(Article)
    author = models.CharField(max_length=80)
    text = models.TextField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)
