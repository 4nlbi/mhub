from django.apps import AppConfig


class HubappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hubapp'

    def ready(self):
        import hubapp.signals  # Import the signals
