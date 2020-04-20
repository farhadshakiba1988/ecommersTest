from django.shortcuts import render

from .models import *


def index(request):

    dest1 = Destinations()
    dest1.name = 'Tehran'
    dest1.img = 'destination_1.jpg'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 800

    dest2 = Destinations()
    dest2.name = 'Tabriz'
    dest2.img = 'destination_2.jpg'
    dest2.desc = 'The City That'
    dest2.price = 700

    dest3 = Destinations()
    dest3.name = 'Shiraz'
    dest3.img = 'destination_3.jpg'
    dest3.desc = 'The City That Never '
    dest3.price = 500

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dest': dests})
