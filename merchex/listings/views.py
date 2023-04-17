from django.http import request, HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {'bands': bands})

def band_detail(request, id): 
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})

def listing_detail (request, id):
    listing = Listing.objects.get(id = id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})
