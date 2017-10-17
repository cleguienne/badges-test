from __future__ import unicode_literals

from django.apps import AppConfig


class ModelsConfig(AppConfig):
    name = 'models3d'

    def ready(self):
        import models3d.signals
