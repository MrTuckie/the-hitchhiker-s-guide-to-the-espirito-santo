from rest_framework import viewsets, serializers
from ..models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()  # type:ignore
    serializer_class = ActivitySerializer
