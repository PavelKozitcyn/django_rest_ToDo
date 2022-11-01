from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import CustomUser


class UserModelSerializers(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_name', 'first_name', 'last_name', 'email']