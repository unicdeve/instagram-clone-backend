from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.api.serializers import UserSerializer

from posts.models import Post, Comment


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {"posted_at": {"read_only": True}}

    def create(self, validated_data):
        user = validated_data.pop("user")

        # user should not create posts for other users
        if self.context["request"].user != user:
            raise serializers.ValidationError(
                "You do not have the permission to perform this action!"
            )

        instance = Post.objects.create(user=user, **validated_data)
        return instance


class PostCustomCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "user", "body", "created_at")
        extra_kwargs = {"created_at": {"read_only": True}}


class PostDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    comments = PostCustomCommentSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "image",
            "alt_text",
            "caption",
            "posted_at",
            "comments",
        )
        extra_kwargs = {"posted_at": {"read_only": True}}


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {"created_at": {"read_only": True}}
