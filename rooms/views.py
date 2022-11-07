from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from rooms import models as room_models
from . import forms


class HomeView(ListView):
  model = room_models.Room
  paginate_by = 10
  paginate_orphans = 5
  ordering = 'created'
  # page_kwarg = 'potato'
  context_object_name = 'rooms'


class RoomDetail(DetailView):
  model = room_models.Room


class SearchView(View):

  def get(self, request):

    country = request.GET.get('country')
    if country:
      # give request.GET to forms.SearchForm() to remember the last options
      form = forms.SearchForm(request.GET)
      if form.is_valid():
        city = form.cleaned_data['city']
        country = form.cleaned_data['country']
        room_type = form.cleaned_data['room_type']
        price = form.cleaned_data['price']
        guests = form.cleaned_data['guests']
        bedrooms = form.cleaned_data['bedrooms']
        beds = form.cleaned_data['beds']
        baths = form.cleaned_data['baths']
        instant_book = form.cleaned_data['instant_book']
        superhost = form.cleaned_data['superhost']
        amenities = form.cleaned_data['amenities']
        facilities = form.cleaned_data['facilities']

        filter_args = {}
        if city != 'Anywhere':
          filter_args['city__startswith'] = city

        filter_args['country'] = country

        if room_type is not None:
          filter_args['room_type'] = room_type

        if price is not None:
          filter_args['price__lte'] = price

        if guests is not None:
          filter_args['guests__gte'] = guests

        if bedrooms is not None:
          filter_args['bedrooms__gte'] = bedrooms

        if beds is not None:
          filter_args['beds__gte'] = beds

        if baths is not None:
          filter_args['baths__gte'] = baths

        if instant_book is True:
          filter_args['instant_book'] = True

        if superhost is True:
          filter_args['host__superhost'] = True

        for s_aminity in amenities:
          filter_args['amenities'] = s_aminity

        for s_facility in facilities:
          filter_args['facilities'] = s_facility

        queryset = room_models.Room.objects.filter(**filter_args).order_by('-created')
        paginator = Paginator(queryset, 10, orphans=5)
        page = request.GET.get('page', 1)
        rooms = paginator.get_page(page)
        return render(request, 'rooms/search.html', {
            'form': form,
            'rooms': rooms
        })

    else:
      form = forms.SearchForm()

    return render(request, 'rooms/search.html', {'form': form})