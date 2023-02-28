from django.urls import path
from . import views

urlpatterns = [
    path("dishes_list/", views.list_dishes, name="dishes_list")
]