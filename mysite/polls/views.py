from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Question 3
def index(request):
    return HttpResponse("Hello World. You are now at the polls index. ")

