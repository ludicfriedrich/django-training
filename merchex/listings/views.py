from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul> 
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')


def contact(request):
    return HttpResponse('<h1>Contactez-vous</h1> <p>Page de contact !</p>')


def listings(request):
    listing = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Liste</h1>
        <ul> 
            <li>{listing[0].title}</li>
            <li>{listing[1].title}</li>
            <li>{listing[2].title}</li>
            <li>{listing[3].title}</li>
        </ul>
    """)
