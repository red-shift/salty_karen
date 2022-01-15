from django.apps import AppConfig


class AppKarenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_karen'

    def ready(self):
        import app_karen.signals
