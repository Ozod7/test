from django.contrib import admin
from .models import Cartoon, Actor, Film, Item


admin.site.register(Cartoon)
admin.site.register(Actor)
admin.site.register(Film)
admin.site.register(Item)