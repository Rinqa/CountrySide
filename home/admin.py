from django.contrib import admin
from .models import Continent,State,Information,Categorie
# Register your models here.
admin.site.register(Continent)
admin.site.register(State)
admin.site.register(Information)
admin.site.register(Categorie)