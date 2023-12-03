from django.http import HttpResponse, Http404
from django.shortcuts import render

from main.models import Car


def test_page(request):
    return HttpResponse('Hello World!')


def cars_list(request):
    cars = Car.objects.all()
    return render(request, 'list.html', {'cars': cars})


def car_details(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        print('ТТТЕЕЕСССТТТТТ', car_id)
        return render(request, 'details.html', {'car': car})
    except Car.DoesNotExist:
        raise Http404('Car not found')
