from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from rooms import models as room_models


def all_rooms(request):
  page = request.GET.get('page', 1)
  room_list = room_models.Room.objects.all()
  paginator = Paginator(room_list, 10, orphans=5)
  try:
    rooms = paginator.page(page)
    return render(request, 'rooms/home.html', {'rooms': rooms})
  except EmptyPage:
    return redirect('/')
