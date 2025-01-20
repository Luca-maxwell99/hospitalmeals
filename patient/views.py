from django.shortcuts import render
from django.http import HttpResponse

def patient(request):
    return HttpResponse("This will manage patient dietary preferences and restrictions")
