from django.shortcuts import render, redirect, reverse, HttpResponse
from catalog.models import Movies
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import messages
from . import mymovies


# Create your views here.


def view_bag(request):
    """A view show a user bag, all code come from code intitute, but they have some slight changes"""
    galeries = Movies.objects.all().order_by('title')
    paginator = Paginator(galeries, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        }
    return render(request, 'bag/bag.html', context)



def push_bag(request, id_movie):
    """A view show a user bag, all code come from code intitute, but they have some slight changes"""


    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if id_movie in list(bag.keys()):
        bag[id_movie] += quantity
    else:
        bag[id_movie] = quantity
    
    request.session['bag'] = bag
    return redirect(redirect_url)

def id_movie(request, id_movie):
    galeries = Movies.objects.all().order_by('id')
    if galeries:
        galeries = Movies.objects.filter(Q(id = id_movie))
        context = {
          'galeries' : galeries 
        }
        return render(request, 'bag/Amovie.html', context)
    return render(request, 'catalog/index.html', context)


def a_movie(request, movie_title):
    galeries = Movies.objects.all().order_by('title')
    if movie_title:
        galeries = Movies.objects.filter(
        Q(title__icontains = movie_title) | Q(release_date__icontains = movie_title)
        ).distinct()
        context = {
          'galeries' : galeries 
        }
        return render(request, 'bag/Amovie.html', context)

def save_movies(request):
    bag = request.session.get('bag',{})
    if not bag:
        messages.warning(request, f'You not have movies in your bag')
        return redirect('bag')
    return render(request,'bag/save_movies.html')


def updata(request, Movies_id):
    """A view show a user bag, all code come from code intitute, but they have some slight changes"""
    Message_Movies = Movies.objects.get(pk=Movies_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag',{})
    a = get_object_or_404(Movies, pk=Movies_id)
    Movies_str_id = str(Movies_id)
    if quantity == 0:
        if Movies_str_id in bag:
            del bag[Movies_str_id]
            messages.error(request, f'The movie has been removed from your bag')
    elif quantity > 0:
        bag[Movies_str_id] = quantity
        messages.success(request, f'The quantity has been updata in your bag')
    request.session['bag'] = bag
    return redirect(reverse('save_movies'))

