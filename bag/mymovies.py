from . import views
from django.shortcuts import render, redirect, reverse
from catalog.models import Movies
from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal





def my_movies(request):
    delivery_fee = 3
    movies_bag = []
    total = 0
    Movies_count = 0
    inbag = request.session.get('bag', {})

    for Movies_id, quantity in inbag.items():
        Movies_cont = get_object_or_404(Movies, pk=Movies_id)
        total += quantity * Movies_cont.price
        Movies_count += quantity
        movies_bag.append({
            'Movies_id': Movies_id,
            'quantity': quantity,
            'total' : total,
            'Movies_cont': Movies_cont,
        })
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = delivery_fee + total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    mycontext = {
        'movies_bag': movies_bag,
        'total': total,
        'Movies_count': Movies_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    
    return mycontext
