from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.accounts.managers import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    """Данные аккаунта"""

    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, unique=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    USERNAME_FIELD = "email"

    objects = AccountManager()

    def __str__(self):
        return f"{self.pk}. {self.email}"

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

