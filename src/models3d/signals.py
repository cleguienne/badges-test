from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

from datetime import timedelta
from models3d.models import Model
from badges.models import Collector, Pioneer

@receiver(post_save, sender=Model)
def model_post_save_collector(sender, created,**kwargs):
    # check a model has been actually created in db
    if created == True:
        user = sender.user.get_queryset().first()
        collector_badge, created = Collector.objects.get_or_create(user=user)
        if sender.objects.filter(user=user).count() >= 5:
            collector_badge.save()

@receiver(post_save, sender=User)
def model_post_save_user(sender, instance, **kwargs):
    date = instance.date_joined
    limit = timezone.now() - timedelta(days=365)
    if  date <= limit:
        pioneer_badge, created = Pioneer.objects.get_or_create(user=instance)
        pioneer_badge.save()