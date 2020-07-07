from django.shortcuts import render

from .models import Order, Category, Producer, Customer


def index(request):
    return render(
        request,
        'platforma/index.html',
    )


def customers(request):

    qs = Customer.objects.all()

    return render(
        request,
        'platforma/customers.html',
        {'header': 'Заказчики', 'customer_card': qs}
    )


def producers(request):

    qs = Producer.objects.all()

    return render(
        request,
        'platforma/producers.html',
        {'header': 'Исполнители', 'producer_card': qs}
    )


def orders(request):

    qs = Order.objects.all()

    return render(
        request,
        'platforma/orders.html',
        {'header': 'Тендеры', 'tender_card': qs}
    )


def categories(request):
    pass
