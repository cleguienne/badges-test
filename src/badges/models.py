from django.db import models
from django.contrib.auth.models import User

class Star(models.Model):
    user = models.ForeignKey(User, unique=True)


class Collector(models.Model):
    user = models.ForeignKey(User, unique=True)


class Pioneer(models.Model):
    user = models.ForeignKey(User, unique=True)
