from django_filters import rest_framework as filters
from .models import Book


# фильтр списка книг по автору, жанру и дате публикации (от даты до другой)
# api/v1/books?author=...&genres=...&from_date=...&to_date=...
class BookFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="publish_date", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="publish_date", lookup_expr="lte")

    class Meta:
        model = Book
        fields = ["author", "genres"]
