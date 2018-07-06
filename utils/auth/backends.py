from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()


class SettingsBackend(object):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'qwerty12345'
    """
    def authenticate(self, request, username=None, password=None):
        try:
            ADMIN_LOGIN = settings.ADMIN_LOGIN
            ADMIN_PASSWORD = settings.ADMIN_PASSWORD
        except AttributeError:
            return None

        login_valid = (ADMIN_LOGIN == username)
        pwd_valid = (ADMIN_PASSWORD == password)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username, email=username, is_staff=True, is_superuser=True)
                user.set_password(ADMIN_PASSWORD)
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
