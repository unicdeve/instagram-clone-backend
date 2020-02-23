from django.db import models
from rest_framework.authtoken.models import Token
from django.db import transaction
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, fullName, password=None):
        email = self.normalize_email(email)
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

    REQUIRED_FIELDS = ["email", "fullName"]
    USERNAME_FIELD = "username"

    objects = UserManager()

    def save(self, *args, **kwargs):

        with transaction.atomic():
            super().save(*args, **kwargs)
            Token.objects.get_or_create(user=self)

    def get_full_name(self):
        return self.fullName

    def get_short_name(self):
        return self.fullName.split(" ")[0]

    def __str__(self):
        return str(self.username) if self.username else ''

    class Meta:
        ordering = ("username",)


class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )
    following_user_id = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ("user_id", "following_user_id")
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"

