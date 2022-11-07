from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from rooms import models as room_models


class HomeView(ListView):
  model = room_models.Room
  paginate_by = 10
  paginate_orphans = 5
  ordering = 'created'
  # page_kwarg = 'potato'
  context_object_name = 'rooms'


class RoomDetail(DetailView):
  model = room_models.Room


def search(request):
  city = request.GET.get('city', 'Anywhere')
  city = str.capitalize(city)
  country = request.GET.get('country', 'KR')
  room_type = int(request.GET.get('room_type', 0))
  room_types = room_models.RoomType.objects.all()

  form = {
      'city': city,
      'selected_room_type': room_type,
      'selected_country': country,
  }

  choices = {
      'countries': countries,
      'room_types': room_types,
  }

  return render(request, 'rooms/search.html', {**form, **choices})
