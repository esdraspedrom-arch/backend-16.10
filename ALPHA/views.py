from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à página inicial do ALPHA!")
def segundapgn(request):
    return HttpResponse("Confira nossos horários de funcionamento!")
