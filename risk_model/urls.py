from django.conf.urls import include, url
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'risk-type', views.RiskTypeViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
]