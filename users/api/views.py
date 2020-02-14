from django.contrib.auth import authenticate, get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from users import models
from .serializers import UserSerializer
from .permissions import UserPermission


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            (token, _) = Token.objects.get_or_create(user=user)

            data = {
                "token": token.key,
                "user_id": user.id,
                "username": user.username,
                "full_name": user.fullName,
                "email": user.email,
            }

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        user = authenticate(request, **request.data)

        if user:
            (token, _) = Token.objects.get_or_create(user=user)

            data = {
                "token": token.key,
                "user_id": user.id,
                "username": user.username,
                "full_name": user.fullName,
                "email": user.email,
            }

            return Response(data, status=status.HTTP_200_OK)

        return Response(
            ["Invalid username/email/password"], status=status.HTTP_400_BAD_REQUEST
        )


class LogoutViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        try:
            Token.objects.get(user=request.user).delete()
        except Token.DoesNotExist:
            pass

        return Response(status=status.HTTP_200_OK)

