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

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Image.search_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-galla/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-galla/search.html',{"message":message})
