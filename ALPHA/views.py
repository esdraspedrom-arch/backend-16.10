from django.shortcuts import render
from django.http import HttpResponse

def home(resquest):
    return HttpResponse("Welcome to the ALPHA home page!")
