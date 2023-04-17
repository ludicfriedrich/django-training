from django.http import request, HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import BandForm
from listings.forms import ListingForm

#List of bands
def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {'bands': bands})

#Detail of selected band
def band_detail(request, id): 
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})

#Create band
def band_create (request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band_detail', band.id)
    else:
        form = BandForm()
    
    return render(request, 'listings/band_create.html', {'form': form})

#About 
def about(request):
    return render(request, 'listings/about.html')

#Contact us
def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email_sent')
    else: 
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})

#Listings
def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})

#Detail listing
def listing_detail (request, id):
    listing = Listing.objects.get(id = id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

#Create listing
def listing_create (request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            
            return redirect('listing_detail', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})

#Email sent
def email_sent (request):
    return render(request, 'listings/email-sent.html')
