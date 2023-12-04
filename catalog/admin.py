from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Book, Genre, Review


class CustomUserAdmin(UserAdmin):
    ordering = ["email"]


admin.site.register(User, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Review)
