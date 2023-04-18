from django.http import request, HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import BandForm
from listings.forms import ListingForm
from django.contrib.auth.models import User, auth
from django.contrib import messages

#Welcome
def welcome(request):
    if request.method == 'POST':
        email = request.POST['email'],
        password = request.POST['password']
    return render(request, 'listings/bands.html')

#Register
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        if not first_name or not last_name or not email or not password:
            messages.info(request, "Tous les champs sont obligatoires")
                
            return redirect('register')
        
        if password == password_confirmation:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Ce nom d'utilisateur existe déjà")
                
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Un utilisateur existe déjà avec cette adresse email")
                
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email = email, first_name = first_name, last_name = last_name)
                user.set_password(password)
                user.save
                print('success')
                return redirect('login')
        else:
            messages.info(request, "Les deux mots de passes ne correspondent pas")
                
            return redirect('register')
                
    else:
        return render(request, 'registration/register.html')

#Login page
def login(request):
    return render(request, 'registration/login.html', {'is_active': 'login'})

#List of bands
def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {'bands': bands, 'is_active': 'band'})

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

#Update band
def band_update(request, id):
        band = Band.objects.get(id=id)
        if request.method == 'POST':
            form = BandForm(request.POST, instance=band)
            if form.is_valid():
                # mettre à jour le groupe existant dans la base de données
                form.save()
                # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
                return redirect('band_detail', band.id)
        else:
            form = BandForm(instance=band)

        return render(request, 'listings/band_update.html', {'form': form})

#Delete band
def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        
        return redirect('band_list')
    
    return render(request, 'listings/band_delete.html', {'band': band})

#About 
def about(request):
    return render(request, 'listings/about.html', {'is_active': 'about'})

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
    return render(request, 'listings/contact.html', {'form': form, 'is_active': 'contact'})

#Listings
def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings, 'is_active': 'listing'})

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

#Update listing
def listing_update (request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance = listing)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', listing.id)
    else:
        form = ListingForm(instance = listing)
    return render(request, 'listings/listing_update.html', {'form': form})

#Email sent
def email_sent (request):
    return render(request, 'listings/email-sent.html')

#Delete listing
def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        listing.delete()
        
        return redirect('listing_list')
    
    return render(request, 'listings/listing_delete.html', {'listing': listing})