from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blogss(request):
    student =[
        {"id": 1, 'name':'mani', 'age':25}
    ]
    return HttpResponse(student)