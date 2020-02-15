import os
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    def image_path_and_rename(self, filename):
        upload_to = "posts/images/"
        name = str(self.created_at) + " " + self.user.username
        new_name = name.replace(" ", "-") + "." + filename.split(".")[-1]
        return os.path.join(upload_to, new_name)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to=image_path_and_rename)
    website = models.CharField(
        max_length=120, verbose_name="Website", null=True, blank=True
    )
    bio = models.CharField(max_length=255, verbose_name="Bio", null=True, blank=True)
    phone_number = models.CharField(
        max_length=20, verbose_name="Phone Number", null=True, blank=True
    )
    gender = models.CharField(max_length=15, verbose_name="Gender")
    followers = models.ManyToManyField(User, related_name='profile_folloers')
    created_at = models.DateTimeField(verbose_name="Created At", auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user.get_short_name()} @{self.user.username}"
