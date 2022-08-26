from django.shortcuts import render
from django.http import HttpResponse

#http://localhost:8000/polls/
def index(request):
    return HttpResponse("Olá, mundo. Você está no índice de enquetes.")