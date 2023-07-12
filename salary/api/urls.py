from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, AdminSalaryViewSet, SalaryViewSet
router = DefaultRouter()


router.register(r'users', UserViewSet)
router.register(r'salary', AdminSalaryViewSet)
router.register(r'salar', SalaryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
