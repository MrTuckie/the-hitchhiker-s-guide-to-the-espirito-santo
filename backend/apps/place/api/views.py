from rest_framework import viewsets, serializers, permissions
from rest_framework.decorators import action
from ..models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"
        depth = 1


class PlaceViewSet(viewsets.ModelViewSet):
    """Essa é a documentação da api de Lugares"""

    queryset = Place.objects.all()  # type: ignore
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
