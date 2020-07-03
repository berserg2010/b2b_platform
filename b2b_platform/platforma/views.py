from django.shortcuts import render
from django.http import HttpResponse

from .models import Tender, Category, Producer, Customer


def index(request):
    return render (request,
                   'platforma/index.html')



def customers(request):
    return render (request,
                   'platforma/customers.html',
                   {
                       'header': 'Заказчики',
                       'customer_card': Customer.objects.all()
                   }

                   )


def producers(request):
    return render (request,
                   'platforma/producers.html',
                   {
                       'header': 'Исполнители',
                       'producer_card': Producer.objects.all()
                   }

                   )


def tenders(request):
    return render (request,
                   'platforma/tenders.html',
                   {
                       'header': 'Тендеры',
                       'tender_card': Tender.objects.all()
                   }

                   )

def categories(request):
    pass