from django.apps import AppConfig


class PatronConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patron'
    verbose_name = 'perfiles'

    def ready(self):
        import patron.signals