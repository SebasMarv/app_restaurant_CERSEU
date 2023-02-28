from django.urls import path
from . import views

urlpatterns = [
    path("waiter_list/", views.list_waiter, name="waiter_list")
]