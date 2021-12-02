from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(res):
    print("Hello")
    return render(res,"contact/index.html")