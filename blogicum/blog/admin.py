from django.contrib import admin
from .models import Category, Post, Location


@admin.register(Category, Location, Post)
class AtAdmin(admin.ModelAdmin):
    pass