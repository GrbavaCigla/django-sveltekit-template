from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


class Preferences(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Preferences.objects.create(owner=instance)
