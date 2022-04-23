
from django.contrib import admin
from . models import house


class houseinfo(admin.ModelAdmin):      
    list_display = ('nom', 'prenom', 'emails' , 'phone')
    search_fields = ['nom', 'prenom']

admin.site.register(house, houseinfo)

# Register your models here.
