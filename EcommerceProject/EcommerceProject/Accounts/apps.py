from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EcommerceProject.Accounts'

    def ready(self):
        import EcommerceProject.Accounts.signals  # This line connects the signals
