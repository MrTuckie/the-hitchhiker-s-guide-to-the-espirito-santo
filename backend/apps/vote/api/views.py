from rest_framework import viewsets, serializers
from ..models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()  # type:ignore
    serializer_class = VoteSerializer
