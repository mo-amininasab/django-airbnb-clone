from django.shortcuts import render
from django.http import HttpResponse
from rooms import models as room_models

def all_rooms(request):
  query = room_models.Room.objects.all()
  context = {
    'rooms': query
  }
  return render(request, 'rooms/home.html', context)


