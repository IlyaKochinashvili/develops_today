from rest_framework import viewsets

from users.models import User
from users.permissions import IsCreationOrIsAuthenticated
from users.serializers import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsCreationOrIsAuthenticated,)

    def get_queryset(self):
        qs = super(UsersViewSet, self).get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(pk=self.request.user.pk)
        return qs
