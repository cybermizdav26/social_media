from django.apps import AppConfig


class FollowerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.follower'

    def ready(self):
        import apps.follower.signals
        