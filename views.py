from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    return HttpResponse("Hello world!")

def members1(request):
  template = loader.get_template('first.html')
  return HttpResponse(template.render())

def members2(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def members3(request):
  template = loader.get_template('master.html')
  return HttpResponse(template.render())