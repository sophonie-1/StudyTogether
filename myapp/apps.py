from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        # Import signals to ensure they are registered when the app is ready
        import myapp.signals
        # # Import views to ensure they are registered when the app is ready
        # import myapp.views
        # # Import models to ensure they are registered when the app is ready
        # import myapp.models
        # # Import forms to ensure they are registered when the app is ready
        # import myapp.forms
        # # Import urls to ensure they are registered when the app is ready
        # import myapp.urls
