from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(blank=False, null=False, max_length=256, unique=True)
    name = models.CharField(blank=False, null=True, max_length=256)
    surname = models.CharField(blank=False, null=True, max_length=256)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        app_label = "catalog"

    def __str__(self) -> str:
        return self.email


class Genre(models.Model):
    name = models.CharField(max_length=64, verbose_name="Genre")

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(
        blank=False, null=False, max_length=256, verbose_name="Title"
    )
    description = models.TextField(blank=False, null=False, verbose_name="Description")
    publish_date = models.DateField(
        blank=False, null=False, verbose_name="Publish date"
    )
    author = models.CharField(max_length=128, verbose_name="Author")
    genres = models.ManyToManyField(Genre, verbose_name="Genres")
    average_rating = models.FloatField(default=0.0, verbose_name="Average rating")

    def __str__(self) -> str:
        return self.title


class Favourite(models.Model):
    book = models.ForeignKey(
        Book, null=False, on_delete=models.CASCADE, verbose_name="Book"
    )
    user = models.ForeignKey(
        User,
        null=False,
        related_name="favourites",
        on_delete=models.CASCADE,
        verbose_name="User",
    )

    def __str__(self) -> str:
        return f"{self.book.title} favourite book of {self.user.email}"


class Review(models.Model):
    book = models.ForeignKey(
        Book, related_name="reviews", on_delete=models.CASCADE, verbose_name="Book"
    )
    user = models.ForeignKey(
        User,
        related_name="reviewed_books",
        on_delete=models.CASCADE,
        verbose_name="User",
    )
    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Rating",
    )
    text = models.TextField(verbose_name="Review's text")

    def __str__(self) -> str:
        return f"{self.user.email} reviewed {self.book.title}"
