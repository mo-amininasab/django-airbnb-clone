from django.views.generic import ListView, DetailView
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

