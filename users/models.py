from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  '''Custom User Model'''

  GENDER_MALE = 'male'
  GENDER_FEMALE = 'female'
  GENDER_OTHER = 'other'

  GENDER_CHOICES = (
      (GENDER_MALE, 'Male'),
      (GENDER_FEMALE, 'Female'),
      (GENDER_OTHER, 'Other'),
  )

  LANGUAGE_ENGLISH = 'en'
  LANGUAGE_KOREAN = 'kr'

  LANGUAGE_CHOICES = (
      (LANGUAGE_ENGLISH, 'English'),
      (LANGUAGE_KOREAN, 'Korean'),
  )

  CURRENCY_USD = 'usd'
  CURRENCY_krw = 'krw'

  CURRENCY_CHOICES = (
      (CURRENCY_USD, 'USD'),
      (CURRENCY_krw, 'KRW'),
  )

  avatar = models.ImageField(blank=True)
  gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)
  bio = models.TextField(blank=True, null=True)
  birthdate = models.DateField(blank=True, null=True)
  language = models.CharField(choices=LANGUAGE_CHOICES,
                              max_length=2,
                              blank=True, null=True)
  currency = models.CharField(choices=CURRENCY_CHOICES,
                              max_length=3,
                              blank=True, null=True)
  superhost = models.BooleanField(default=False)