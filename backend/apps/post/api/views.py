from rest_framework import viewsets, serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostViewSet(viewsets.ModelViewSet):
    """viewsets de posts"""

    queryset = Post.objects.all()  # type:ignore
    serializer_class = PostSerializer
