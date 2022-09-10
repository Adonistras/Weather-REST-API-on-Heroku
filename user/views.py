from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import UserAPI
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsYourProfile


class ListUsers(viewsets.GenericViewSet):
    queryset = UserAPI.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def list(self, request):
        serializer = UserSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(UserAPI, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class RetrieveUpdateUserAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAPI.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsYourProfile, IsAdminUser)


class CreateUserAPI(generics.CreateAPIView):
    queryset = UserAPI.objects.all()
    serializer_class = UserCreateSerializer









