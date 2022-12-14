import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models
from reservations import models as reservation_models

NAME = 'reservations'


class Command(BaseCommand):
  help = f'This command creates many {NAME}'

  def add_arguments(self, parser):
    parser.add_argument(
        '--number',
        default=1,  # not working???
        type=int,
        help=f'How many {NAME} do you want to create')

  def handle(self, *args, **options):
    number = options.get('number')
    seeder = Seed.seeder()

    users = user_models.User.objects.all()
    rooms = room_models.Room.objects.all()

    now = datetime.now()
    seeder.add_entity(
        reservation_models.Reservation,
        number,
        {
            'status':
            lambda x: random.choice(['pending', 'confirmed', 'canceled']),
            'guest': lambda x: random.choice(users),
            'room': lambda x: random.choice(rooms),
            'check_in': lambda x: now,  # timezone doesn't matter here
            'check_out': lambda x: now + timedelta(days=random.randint(3, 25))
        })
    seeder.execute()

    self.stdout.write(self.style.SUCCESS(f'{number} {NAME} created!'))
