from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    customized User model
    """
    class Meta(AbstractUser.Meta):
        db_table = 'user'
        swappable = 'AUTH_USER_MODEL'
