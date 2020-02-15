import os
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    def photo_path_and_rename(self, filename):
        upload_to = "posts/images/"
        name = str(self.user) + " " + self.user.username
        new_name = name.replace(" ", "-") + "." + filename.split(".")[-1]
        return os.path.join(upload_to, new_name)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to=photo_path_and_rename)
    alt_text = models.CharField(max_length=120, blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    # video_url = models.CharField(max_length=255, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True, verbose_name="Posted At")

    class Meta:
        ordering = ("posted_at",)

    def __str__(self):
        return self.user

