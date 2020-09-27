
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpRequest
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from catalog.models import Movies
from .models import order, OrderLineItem
from bag.mymovies import my_movies
import stripe
# This is your real test secret API key.

   

# Create your views here.
def checkout(request):
    stripe_public_key = 'pk_test_0p4jqeiFYPzrkeRsn0iQdaSO00VNNlhS7K'#settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = 'sk_test_RTba6nZ1WHPp4rAX65VasJL600Uc7R8pg2'#settings.STRIPE_SECRET_KEY
    print(my_movies)
    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'county': request.POST['county'],
            'postcade': request.POST['postcade'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],

        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            print(order)
            print("profundidad 1")
            for Movies_id, quantity in bag.items():
                print(Movies_id)
                print("profundidad 2")
                try:
                    movie = Movies.objects.get(id= Movies_id)
                    print(movie)
                    print("profundidad 3")
                    if isinstance(quantity, int):
                        Order_Line = OrderLineItem(
                            order=order,
                            Movie= movie,
                            quantity=quantity,
                        )
                        print("profundidad 4")
                        print(Order_Line)
                        line = OrderForm(Order_Line)
                        line.save()
                except Movies.DoesNotExist:
                    messages.error(request, " The movie not exist, the order will be cancel")
                    order.delete()
                    return redirect(reverse('bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('bag'))
        the_bag = my_movies(request)
        total = the_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(amount=stripe_total, currency=settings.STRIPE_CURRENT)
        order_form = OrderForm()
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
        'intent':intent,
    }

    return render(request, template, context)



def checkout_success(request, order_number):
    save_info = request.session.get('save_info',{})
    print(save_info)
    #success_order = get_object_or_404(Movies, order_number=order_number)
    #messages.success(request, f'Thanks for your shopping, your number order is {Order.order_number}, we send you a email at {Order.email}')

    if 'bag' in request.session:
        del request.session['bag']
    
    template = 'checkout_success.html'

    context = {
        'order' : order,
    }

    return render (request, template, context) 


