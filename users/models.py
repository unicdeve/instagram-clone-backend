from django.db import models
from rest_framework.authtoken.models import Token
from django.db import transaction
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManger(BaseUserManager):
    def create_user(self, email, username, fullName, password=None):
        user = self.model(email=email, username=username, fullName=fullName)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, fullName, password):
        user = self.create_user(email, username, fullName, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="E-mail")
    username = models.CharField(max_length=120, unique=True, verbose_name="Username")
    fullName = models.CharField(max_length=120, verbose_name="Full name")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["fullName", "email"]
    USERNAME_FIELD = "username"

    objects = UserManger()

    def save(self, *args, **kwargs):

        with transaction.atomic():
            super().save(*args, **kwargs)
            Token.objects.get_or_create(user=self)

    def get_full_name(self):
        return self.fullName

    def get_short_name(self):
        return self.fullName.split(" ")[0]

    def __str__(self):
        return f"@{self.username}"

    class Meta:
        ordering = ("username",)

