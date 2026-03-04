from rest_framework import permissions, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.views import Response, status

from apps.post.api.views import PostSerializer

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
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=["post"])
    def add_post(self, request, pk=None):
        """
        TODO: Finish this function
        funçao para adicionar posts para um lugar
        TODO: Como o queryset é apenas Place, o endpoint daqui
        só vai expor o campo name (pois place só tem name mesmo).
        |Tem quem ver isso daí chefia.
        """
        place = Place.objects.get(id=pk)
        serializer = PostSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save(place=place)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"message": f"{serializer.error_messages}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
