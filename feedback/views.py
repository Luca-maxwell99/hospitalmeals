from django.shortcuts import render
from django.http import HttpResponse

def feedback(request):
    return HttpResponse('Collect and manage feedback')