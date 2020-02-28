from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.api.serializers import UserSerializer

from posts.models import Post, Comment, LikePost, LikeComment
from profiles.models import Profile


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


class CustomCommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = ("id", "user", "liked_at")
        extra_kwargs = {"liked_at": {"read_only": True}}


class CustomProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'image', )


class CustomCommentUserSerializer(serializers.ModelSerializer):
    profile = CustomProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'fullName', 'profile')


class PostCustomCommentSerializer(serializers.ModelSerializer):
    likes = CustomCommentLikeSerializer(many=True)
    user = CustomCommentUserSerializer(many=False)

    class Meta:
        model = Comment
        fields = ("id", "user", "body", "created_at", "likes")
        extra_kwargs = {"created_at": {"read_only": True}}


class PostCustomLikePostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = LikePost
        fields = ("id", "user", "liked_at")
        extra_kwargs = {"liked_at": {"read_only": True}}


class CustomUserSerializer(serializers.ModelSerializer):
    profile = CustomProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'fullName', 'profile')


class PostDetailsSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(many=False)
    comments = PostCustomCommentSerializer(many=True)
    likes = PostCustomLikePostSerializer(many=True)

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
            "likes",
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


class LikePostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = LikePost
        fields = "__all__"
        extra_kwargs = {"liked_at": {"read_only": True}}


class LikeCommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = LikeComment
        fields = "__all__"
        extra_kwargs = {"liked_at": {"read_only": True}}
