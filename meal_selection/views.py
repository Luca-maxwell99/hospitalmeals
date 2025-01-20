from django.shortcuts import render
from django.http import HttpResponse

def selection(request):
    return HttpResponse('allows patients or careers to select and confirm meals')
