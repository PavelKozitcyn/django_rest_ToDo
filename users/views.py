from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserModelSerializers


# Create your views here.
class UserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializers

