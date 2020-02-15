from rest_framework import serializers
from django.contrib.auth import get_user_model

from profiles.models import Profile
from users.api.serializers import UserSerializer


User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    # adding request.user automatically
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Profile
        fields = "__all__"
        extra_kwargs = {"created_at": {"read_only": True}}

    def create(self, validated_data):
        user = validated_data.pop("user")

        # user should not create profile for other users
        if self.context["request"].user != user:
            raise serializers.ValidationError(
                "You do not have the permission to perform this action!"
            )

        # check if user already exists
        user_exists = Profile.objects.filter(user=user).first()
        if user_exists:
            raise serializers.ValidationError("Profile with this User already exists.")

        instance = Profile.objects.create(user=user, **validated_data)
        return instance


# Serializer for GET Profile with full User
class ProfileUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Profile
        fields = "__all__"
        extra_kwargs = {"created_at": {"read_only": True}}

    def create(self, validated_data):
        pass
