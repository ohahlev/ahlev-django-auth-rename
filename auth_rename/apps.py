from django.contrib.auth.apps import AuthConfig


class AuthRenameConfig(AuthConfig):
    verbose_name = 'User Management'
