from rest_framework import serializers
from .models import Genre, Book, Review, Favourite, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "name", "surname")
        extra_kwargs = {"password": {"write_only": True}}


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField()
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

    def get_is_favorite(self, obj):
        user = self.context["request"].user
        return Favourite.objects.filter(user=user, book=obj).exists()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = "__all__"
