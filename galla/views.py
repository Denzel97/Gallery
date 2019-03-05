from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Location,Category,Image

import datetime as dt

# Create your views here.
def welcome(request):
    all_images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Home'
    return render(request, 'index.html',{'all_images':all_images,'locations':locations,'categories':categories, 'title':title})

def galla_today(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'all-galla/today-galla.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def search_results(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("title")
        searched_locations = Location.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})


def past_days_galla(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(galla_of_day)

    return render(request, 'all-galla/past-galla.html', {"date": date})
