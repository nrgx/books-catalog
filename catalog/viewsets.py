from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404
from .filters import BookFilter
from .models import (
    Genre,
    Book,
    Review,
    Favourite,
)
from .serializers import (
    GenreListSerializer,
    BookSerializer,
    ReviewSerializer,
    FavouriteSerializer,
)
from .service import BookService


class GenreAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = GenreListSerializer
    queryset = Genre.objects.all()


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        book_id = self.request.data["book"]
        book = get_object_or_404(Book, id=book_id)
        serializer.save(book=book)
        BookService.calculate_avg_rating(book=book)


class FavouriteViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
