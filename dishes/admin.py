from django.contrib import admin

# Register your models here.
from .models import Dishes

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_display = ("name","price",)
    list_filter = ("name",)