from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Blog


def blogs(request):
  blogs= Blog.objects.all().values()
  template = loader.get_template('blogs.html')
  context = {
  'blogs': blogs,
  }
  return HttpResponse(template.render(context,request))