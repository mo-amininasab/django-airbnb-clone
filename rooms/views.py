from django.shortcuts import render
from django.core.paginator import Paginator
from rooms import models as room_models

def all_rooms(request):
  page = request.GET.get('page')
  room_list = room_models.Room.objects.all()
  paginator = Paginator(room_list, 10)
  rooms = paginator.get_page(page)

  context = {
    'rooms': rooms
  }
  return render(request, 'rooms/home.html', context)


