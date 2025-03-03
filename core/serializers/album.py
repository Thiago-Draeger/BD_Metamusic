from rest_framework.serializers import ModelSerializer
from core.models import Album

class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"