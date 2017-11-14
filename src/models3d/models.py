from django.db import models
from django.contrib.auth.models import User

from badges.models import Star, Collector


class Model(models.Model):
    name = models.CharField(max_length=48)
    file = models.FileField(upload_to='uploads/', max_length=256)
    user = models.ForeignKey(User, related_name='models')
    vertice_count = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    hits = models.IntegerField(default=0)

    def add_visit(self):
        self.hits += 1
        if self.hits >= 100:
            star_badge, created = Star.objects.get_or_create(user=self.user)
            star_badge.save()
