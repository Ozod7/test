from django.urls import path
from . import views
def item_list(request):
    items = Item.objects.all()
    return render(request, "shop/item_list.html", {"items": items})

urlpatterns = [
    path("", views.home, name="home"),

    path("cartoons/", views.cartoon_list, name="cartoon_list"),
    path("cartoon/<int:pk>/", views.cartoon_detail, name="cartoon_detail"),

    path("films/", views.film_list, name="film_list"),
    path("film/<int:pk>/", views.film_detail, name="film_detail"),

    path("actor/<int:pk>/", views.actor_detail, name="actor_detail"),

    path("actors/", views.actor_list, name="actor_list"),
    path("items/", views.item_list, name="item_list"),
]