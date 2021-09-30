from django.contrib import admin
from .models import Image


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    pass
