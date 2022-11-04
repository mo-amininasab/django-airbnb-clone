from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
  print('hello')

  def handle(self, *args, **options):
    amenities = [
        'TV',
        'Towels',
        'Toilet',
        'Swimming pool',
        'Stereo',
        'Sofa',
        'Smoke detectors',
        'Shoppings Mall',
        'Restaurant',
        'Oven',
        'Outdoor Pool',
    ]
    for a in amenities:
      Amenity.objects.create(name=a)
    self.stdout.write(self.style.SUCCESS('Amenities created!'))