from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.api.serializers import UserSerializer

from posts.models import Post


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


class PostDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {"posted_at": {"read_only": True}}
