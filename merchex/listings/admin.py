from django.contrib import admin
from listings.models import Band
from listings.models import Listing
from listings.models import Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste
    
class ListingAdmin (admin.ModelAdmin):
    list_display = ('title','year', 'sold')

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Listing, ListingAdmin)