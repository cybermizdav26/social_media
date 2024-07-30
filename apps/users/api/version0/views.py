from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.users.api.version0.serializers import UserCreateSerializer, UserUpdateSerializer, UserSerializer

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)


user_create = UserCreateAPIView.as_view()


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'pk'


user_update = UserUpdateAPIView.as_view()


class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'  # Default lookup field is 'pk'


user_delete = UserDestroyView.as_view()



