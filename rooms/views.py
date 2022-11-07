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

  price = int(request.GET.get('price', 0))
  guests = int(request.GET.get('guests', 0))
  bedrooms = int(request.GET.get('bedrooms', 0))
  beds = int(request.GET.get('beds', 0))
  baths = int(request.GET.get('baths', 0))

  instant = request.GET.get('instant', False)
  super_host = request.GET.get('super_host', False)
  print(instant, super_host)

  selected_amenities = request.GET.getlist('amenities')
  selected_facilities = request.GET.getlist('facilities')

  form = {
      'city': city,
      'selected_room_type': room_type,
      'selected_country': country,
      'price': price,
      'guests': guests,
      'bedrooms': bedrooms,
      'beds': beds,
      'baths': baths,
      'instant': instant,
      'super_host': super_host,
      'selected_amenities': selected_amenities,
      'selected_facilities': selected_facilities,
  }

  room_types = room_models.RoomType.objects.all()
  amenities = room_models.Amenity.objects.all()
  facilities = room_models.Facility.objects.all()
  choices = {
      'countries': countries,
      'room_types': room_types,
      'amenities': amenities,
      'facilities': facilities,
  }

  return render(request, 'rooms/search.html', {**form, **choices})
