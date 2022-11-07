from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from rooms import models as room_models


class HomeView(ListView):
  model = room_models.Room
  paginate_by = 10
  paginate_orphans = 5
  ordering = 'created'
  # page_kwarg = 'potato'
  context_object_name = 'rooms'


or make it more professional
