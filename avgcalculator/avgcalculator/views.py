rom django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Avg Calc")