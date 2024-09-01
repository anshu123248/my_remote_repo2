from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s='<h1>Welcome to Durga django classes...purely nursely level classes</h1>'
    return HttpResponse(s)
