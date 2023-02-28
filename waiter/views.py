from django.shortcuts import render
from waiter.models import Waiter
from django.db.models import F,Q

# Create your views here.
def list_waiter(request):
    # waiters = Waiter.objects.all()
    query = Q(provenance__startswith='Pe')
    waiters = Waiter.objects.filter(query, years__lt=30)
    Waiter.objects.filter(years__lt=27).update(years=(F('years') + 5))
    return render(request, 'waiter/waiter_list.html', context={'data':waiters})