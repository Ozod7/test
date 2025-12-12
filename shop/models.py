from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Cartoon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    image_url = models.URLField(blank=True)

    actors = models.ManyToManyField(Actor, related_name="cartoons", blank=True)

    def __str__(self):
        return self.title


class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    image_url = models.URLField(blank=True)

    actors = models.ManyToManyField(Actor, related_name="films", blank=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    cartoon = models.ForeignKey(
        Cartoon,
        on_delete=models.CASCADE,
        related_name="items"
    )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name