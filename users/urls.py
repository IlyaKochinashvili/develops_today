from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
