from django.views.generic import ListView
from django.shortcuts import render
from rooms import models as room_models

class HomeView(ListView):
  model = room_models.Room
  paginate_by = 10
  paginate_orphans = 5
  ordering = 'created'
  # page_kwarg = 'potato'
  context_object_name = 'rooms'

def room_detail(request, pk):
  return render(request, 'rooms/detail.html', {})

  
