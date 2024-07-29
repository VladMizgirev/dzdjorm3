from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale


def cars_list_view(request):
    cars = Car.objects.all()
    template_name = 'main/list.html'
    return render(request, template_name, {"cars_list": cars})


def car_details_view(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        template_name = 'main/details.html'
        return render(request, template_name, {'car': car})
    except Car.DoesNotExist:
        raise Http404('Car not found')



def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.all().filter(car=car_id)
        template_name = 'main/sales.html'
        return render(request, template_name, {"car": car, "sales": sales})  
    except Car.DoesNotExist:
        raise Http404('Car not found')
