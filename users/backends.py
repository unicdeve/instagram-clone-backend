from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


User = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    # def authenticate(self, request, username=None, password=None):
    #     print("working herrrrrrree")
    #     try:
    #         user = User.objects.filter(
    #             Q(username__iexact=username) | Q(email__iexact=username)
    #         ).distinct()
    #         print(user)

    #     except User.DoesNotExist:
    #         return None

    #     else:
    #         if user.exists():
    #             user_obj = user.first()
    #             print(user_obj)
    #             if user_obj.check_password(password):
    #                 return user_obj
    #             return None

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username)
            )
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

