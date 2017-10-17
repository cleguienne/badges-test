from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

from datetime import timedelta
from models3d.models import Model
from badges.models import Collector, Pioneer

@receiver(post_save, sender=Model)
def model_post_save_collector(sender, **kwargs):
    # check a model has been actually created in db
    if kwargs['created'] == True:
        user = sender.user.get_queryset().first()
        if Collector.objects.filter(user=user).count() == 0:
            if sender.objects.filter(user=user).count() >= 5:
                collector_badge = Collector.objects.create(user=user)
                collector_badge.save()

@receiver(post_save, sender=User)
def model_post_save_user(sender, **kwargs):
    user = kwargs.get('instance')
    date = user.date_joined
    limit = timezone.now() - timedelta(days=365)
    if  date <= limit:
        if Pioneer.objects.filter(user=user).count() == 0:
            pioneer_badge = Pioneer.objects.create(user=user)
            pioneer_badge.save()