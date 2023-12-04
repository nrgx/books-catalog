from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .viewsets import *


router = DefaultRouter(trailing_slash=False)
router.register(r"books", BookViewSet, "books")
router.register(r"genres", GenreAPIView, "genres")
router.register(r"reviews", ReviewViewSet, "reviews")
router.register(r"favourites", FavouriteViewSet, "favourites")

urlpatterns = router.urls
