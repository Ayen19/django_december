from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods



# Create your views here.

def read_contacts(res):
    print(res)
    print("reading contacts...")
    return render(res,"contact/index.html")


def read_contact(res,id):
    #find out other ways of string concats
    print(f"reading contact...{id}")
    return render(res,"contact/index.html")


# @csrf_exempt
def create_contact(res):
    print("creating contact...")
    return render(res,"contact/index.html")


# @csrf_exempt
def edit_contact(res,id):
    print(f"editing contact...{id}")
    return render(res,"contact/index.html")


def delete_contact(res,id):
    print(f"deleting contact...{id}")
    return render(res,"contact/index.html")