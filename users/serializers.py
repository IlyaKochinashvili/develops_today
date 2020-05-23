from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'pk', 'email', 'password',)
        write_only = ('password',)
        read_only = ('pk',)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            is_staff=False,
            is_active=True,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
