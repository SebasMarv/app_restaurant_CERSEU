from django.urls import path
from . import views

urlpatterns = [
    path("customer_list/", views.list_customer, name="customer_list")
]