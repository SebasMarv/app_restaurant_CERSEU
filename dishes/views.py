from django.shortcuts import render
from dishes.models import Dishes
from django.db.models import F,Q

# Create your views here.
def list_dishes(request):
    # dishess = Dishes.objects.all()
    query = Q(provenance__startswith='Pe')
    dishess = Dishes.objects.filter(query, price__gt=40)
    return render(request, 'dishes/dishes_list.html', context={'data':dishess})