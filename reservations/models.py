from django.db import models
from django.utils import timezone
from core import models as core_models


class Reservation(core_models.TimeStampedModel):
  STATUS_PENDING = 'pending'
  STATUS_CONFIRMED = 'confirmed'
  STATUS_CANCELED = 'canceled'

  STATUS_CHOICES = (
      (STATUS_PENDING, 'Pending'),
      (STATUS_CONFIRMED, 'confirmed'),
      (STATUS_CANCELED, 'canceled'),
  )

  status = models.CharField(max_length=12,
                            choices=STATUS_CHOICES,
                            default=STATUS_PENDING)
  guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
  room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
  check_in = models.DateField(auto_now=False, auto_now_add=False)
  check_out = models.DateField(auto_now=False, auto_now_add=False)

  def __str__(self):
    return f'{self.room} - {self.check_in}'

  def in_progress(self):
    now = timezone.now().date()
    return self.check_in <= now <= self.check_out

  in_progress.boolean = True

  def is_finished(self):
    now = timezone.now().date()
    return now > self.check_out

  is_finished.boolean = True
