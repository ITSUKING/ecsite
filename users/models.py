from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザモデル"""
    initial_point = 50000
    email = models.EmailField("メールアドレス", unique=True)
    point = models.PositiveIntegerField(default=initial_point)
    is_staff = models.BooleanField("is_staff", default=False)
    is_active = models.BooleanField("is_active", default=True)
    date_joined = models.DateTimeField("date_joined",
                                       default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
