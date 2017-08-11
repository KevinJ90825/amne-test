from django.shortcuts import render
from django.conf import settings


def index(request):
    context = {
        'PLACES_API_KEY': settings.GOOGLE_PLACES_KEY
    }

    return render(request, 'main/index.html', context)