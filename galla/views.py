from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Location,Category,Image

import datetime as dt

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Gallery'
    return render(request, 'index.html',{'images':images,'locations':locations,'categories':categories, 'title':title})

def search_results(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("title")
        searched_locations = Location.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
