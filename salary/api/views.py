from rest_framework import viewsets
from post.models import User, Salary
from api.serializers import (CustomUserSerializer,
                             AdminSalarySerializer,
                             SalarySerializer)
from api.permissions import WorkerOrReadOnly, ReadOnly
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminUser,)


class AdminSalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = AdminSalarySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminUser,)


class SalaryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = (WorkerOrReadOnly,)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def get_quetyset(self):
        worker_id = self.get("worker_id")
        new_queryset = Salary.objects(worker=worker_id)
        return new_queryset
