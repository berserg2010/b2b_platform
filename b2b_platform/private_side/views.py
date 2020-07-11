from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse


@login_required
def main(request):
    return HttpResponse(
        'You are enter'
    )


@login_required
def customers():
    pass


@login_required
def producers():
    pass
