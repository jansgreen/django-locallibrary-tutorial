from django.shortcuts import render, redirect, reverse
from catalog.models import Movies
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.


def view_bag(request):
    """ A view that render """

    search = request.GET.get("Search")
    galeries = Movies.objects.all().order_by('title')
    if search:
        galeries = Movies.objects.filter(
            Q(title__icontains = search) | Q(release_date__icontains = search)
            ).distinct()
            
        if not galeries:
            messages.add_message(request, messages.INFO, 'The movie '+search+' you looking far is not found!')
    paginator = Paginator(galeries, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        }
    return render(request, 'index.html', context)

def push_bag(request, id_movie):
    print(id_movie)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if id_movie in list(bag.keys()):
        bag[id_movie] += quantity
    else:
        bag[id_movie] = quantity
    
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(request,redirect_url)

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

