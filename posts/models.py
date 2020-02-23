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
        ordering = ("-posted_at",)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.CharField(max_length=255, verbose_name="Comment body")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At", db_index=True
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user.username} commented on {self.post}'s post"


class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    liked_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("liked_at",)
        unique_together = ("user", "post")

    def __str__(self):
        return f"{self.user.username} liked {self.post.user.username}'s post"


class LikeComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comment_likes"
    )
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
    liked_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("liked_at",)
        unique_together = ("user", "comment")

    def __str__(self):
        return f"{self.user.username} liked {self.comment.user.username}'s post"
