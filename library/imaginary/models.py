from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.title}"


class Book(models.Model):
    LANGUAGES = (
        ("AZ", "AZ"),
        ("EN", "EN"),
        ("RU", "RU")
    )

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    published_at = models.PositiveIntegerField()
    language = models.CharField(max_length=4, choices=LANGUAGES)
    rating = models.FloatField()
    price = models.PositiveIntegerField()
    page_count = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.title}"
