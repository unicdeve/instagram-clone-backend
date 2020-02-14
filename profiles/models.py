from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(
        max_length=120, verbose_name="Website", null=True, blank=True
    )
    bio = models.CharField(max_length=255, verbose_name="Bio", null=True, blank=True)
    phone_number = models.CharField(
        max_length=20, verbose_name="Phone Number", null=True, blank=True
    )
    gender = models.CharField(max_length=15, verbose_name="Gender")
    created_at = models.DateTimeField(verbose_name="Created At", auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user.get_short_name()} @{self.user.username}"
