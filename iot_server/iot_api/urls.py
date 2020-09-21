from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, DataViewSet

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', DataViewSet, base_name='data')
urlpatterns = router.urls
