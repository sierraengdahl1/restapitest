from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'input', views.InputViewSet)
#router.register(r'input/', InputViewSet, basename='Input' )

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
