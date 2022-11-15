from django.db import models

from django.contrib.auth.models import (AbstractUser)

class AppUser(AbstractUser):
    """AppUser model - user account"""
    email = models.EmailField(
        verbose_name='email address', # optional argument
        max_length=255,
        unique=True
    )

    is_active = models.BooleanField(default=True)

    # The `password` field is built in to AbstractUser

    # For Django, the `username` field is special for User models
    # It is what is used for login.
    # If we just want to use email for login, and not require a username,
    # We have to tell Django to treat the `email` field like the `username` field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # email and password are required by default


