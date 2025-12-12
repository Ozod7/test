from django.contrib import admin
from .models import Cartoon, Actor, Film, Item, Review


admin.site.register(Cartoon)
admin.site.register(Actor)
admin.site.register(Film)
admin.site.register(Item)
admin.site.register(Review)