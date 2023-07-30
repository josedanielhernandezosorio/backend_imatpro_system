from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from com.sofyntelligen.imatpro.app.model.system.equations.system.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'get_avatar',
                  'is_active',
                  'is_staff',
                  'is_superuser',
                  'groups',
                  'user_permissions',
                  )
