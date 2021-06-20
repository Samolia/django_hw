from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = [station for station in reader]
        page = int(request.GET.get('page', 1))
        stations_per_page = 10
        paginator = Paginator(stations, stations_per_page)
        page_ = paginator.get_page(page)
        content = page_.object_list
        context = {
            'bus_stations': content,
            'page': page_,
        }
        return render(request, 'stations/index.html', context)
