from django.shortcuts import render
from customer.models import Customer
# from django.db.models import F,Q

# Create your views here.
def list_customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', context={'data':customers})