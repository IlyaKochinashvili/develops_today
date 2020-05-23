from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from posts.views import PostsViewSet, CommentsViewSet, PostApiView

router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentsViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('posts/upvotes/<int:pk>/', PostApiView.as_view())
]