
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.mymovies import my_movies
import stripe
# This is your real test secret API key.



# Create your views here.
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('Movies'))
    the_bag = my_movies(request)
    total = the_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(amount=stripe_total, currency=settings.STRIPE_CURRENT)
    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key' : stripe_public_key,
        'client_secret' : stripe_secret_key,
    }

    return render(request, template, context)