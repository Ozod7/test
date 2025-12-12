from django.shortcuts import render, get_object_or_404
from .models import Cartoon, Film, Actor

def home(request):
    cartoons = Cartoon.objects.all()
    films = Film.objects.all()
    return render(request, "shop/home.html", {
        "cartoons": cartoons,
        "films": films,
    })


def cartoon_list(request):
    return render(request, "shop/cartoon_list.html", {
        "cartoons": Cartoon.objects.all()
    })


def film_list(request):
    return render(request, "shop/film_list.html", {
        "films": Film.objects.all()
    })


def cartoon_detail(request, pk):
    cartoon = get_object_or_404(Cartoon, pk=pk)
    return render(request, "shop/cartoon_detail.html", {
        "cartoon": cartoon,
        "actors": cartoon.actors.all(),
        "items": cartoon.items.all()
    })


def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, "shop/film_detail.html", {
        "film": film,
        "actors": film.actors.all()
    })


def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    return render(request, "shop/actor_detail.html", {
        "actor": actor,
        "films": actor.films.all(),
        "cartoons": actor.cartoons.all()
    })