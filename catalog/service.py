from .models import Book, Review


# Сервис для расчета среднего рейтинга на книгу.
# Вызов при создании рейтинга.
class BookService:
    @staticmethod
    def calculate_avg_rating(book: Book):
        reviews = Review.objects.filter(book=book)
        if reviews.exists():
            total = sum(review.rating for review in reviews)
            average = total / len(reviews)
            book.average_rating = average
            book.save()
