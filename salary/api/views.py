from rest_framework import viewsets
from post.models import User, Salary
from api.serializers import (CustomUserSerializer,
                             AdminSalarySerializer,
                             SalarySerializer)
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.decorators import action


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

    @action(detail=False, url_path='recent')
    def get_worker(self, request):
        work = Salary.objects.filter(worker=request.user)
        serializer = self.get_serializer(work, many=True)
        return Response(serializer.data)
