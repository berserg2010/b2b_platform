from django.urls import path

from .views import main, customers, producers


app_name = 'private_side'

urlpatterns = [
    path('', main, name='main'),

    path('customers', customers, name='customers'),


    path('producers', producers, name='producers'),
]
