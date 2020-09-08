from django.urls import path,include
from django.conf.urls import url

from .views import BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BookingViewSet)


urlpatterns = [

]

urlpatterns += router.urls