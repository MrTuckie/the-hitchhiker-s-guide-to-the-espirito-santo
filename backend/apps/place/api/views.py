from rest_framework import views, viewsets, serializers
from ..models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class PlaceViewSet(viewsets.ModelViewSet):
    """Essa é a documentação da api de Lugares"""

    queryset = Place.objects.all()  # type: ignore
    serializer_class = PlaceSerializer
