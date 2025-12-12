from django.shortcuts import render, get_object_or_404
from .models import Cartoon, Film, Actor, Item, Review


def home(request):
    cartoons = Cartoon.objects.all()
    films = Film.objects.all()
    actors = Actor.objects.all()
    items = Item.objects.all()

    return render(request, "shop/home.html", {
        "cartoons": cartoons,
        "films": films,
        "actors": actors,
        "items": items,
    })


def cartoon_list(request):
    cartoons = Cartoon.objects.all()
    return render(request, "shop/cartoon_list.html", {"cartoons": cartoons})


def film_list(request):
    films = Film.objects.all()
    return render(request, "shop/film_list.html", {"films": films})


def actor_list(request):
    actors = Actor.objects.all()
    return render(request, "shop/actor_list.html", {"actors": actors})


def item_list(request):
    items = Item.objects.all()
    return render(request, "shop/item_list.html", {"items": items})


def cartoon_detail(request, pk):
    cartoon = get_object_or_404(Cartoon, pk=pk)
    return render(request, "shop/cartoon_detail.html", {"cartoon": cartoon})


def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, "shop/film_detail.html", {"film": film})


def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    films = actor.films.all()
    cartoons = actor.cartoons.all()
    return render(request, "shop/actor_detail.html", {
        "actor": actor,
        "films": films,
        "cartoons": cartoons
    

    })
    
def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)

    if request.method == 'POST':
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        text = request.POST.get('text')

        review = Review.objects.create(
            author=author,
            rating=rating,
            text=text,
            film=film
        )
        return redirect('film_detail', pk=film.pk)

    reviews = film.reviews.all()
    return render(request, "shop/film_detail.html", {"film": film, "reviews": reviews})