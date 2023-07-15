from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']


User._meta.get_field('email').null = False
User._meta.get_field('email').blank = False
User._meta.get_field('email')._unique = True

User._meta.get_field('first_name').null = False
User._meta.get_field('first_name').blank = False

User._meta.get_field('last_name').null = False
User._meta.get_field('last_name').blank = False


class Preferences(models.Model):
    owner = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        Preferences.objects.create(owner=instance)
