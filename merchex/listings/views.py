from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>Contactez-vous</h1> <p>Page de contact !</p>')

def articles(request):
    return HttpResponse('<h1>Articles</h1> <p>Nos articles !</p>')