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
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Указан decimal_places
    cartoon = models.ForeignKey(Cartoon, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.CharField(max_length=100)  
    text = models.TextField()  
    rating = models.PositiveSmallIntegerField(default=5)  
    created_at = models.DateTimeField(auto_now_add=True)  

    
    film = models.ForeignKey(
        'Film',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='reviews'
    )

    cartoon = models.ForeignKey(
        'Cartoon',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='reviews'
    )

    def __str__(self):
        return f'{self.author} — {self.rating}/5'