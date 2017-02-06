from django.http import HttpResponse
from django.views.list import ListView
from models import Restaurants


def home(request):
    return HttpResponse("Restaurant Landing Page.")
