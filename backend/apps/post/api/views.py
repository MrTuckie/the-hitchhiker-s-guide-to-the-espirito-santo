from django.db.models import Count, Q
from rest_framework import viewsets, serializers, filters
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    place = serializers.StringRelatedField(read_only=True)
    upvotes = serializers.IntegerField(read_only=True)
    downvotes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class PostViewSet(viewsets.ModelViewSet):
    """viewsets de posts"""

    serializer_class = PostSerializer
    filterset_fields = ("place", "created_at")
    filter_backends = (filters.OrderingFilter,)
    ordering = ("-created_at",)

    def get_queryset(self):
        return Post.objects.annotate(
            # Count only where upvote=True
            upvotes=Count("votes", filter=Q(votes__upvote=True)),
            # Count only where upvote=False
            downvotes=Count("votes", filter=Q(votes__upvote=False)),
        ).order_by("-upvotes")  # You can order by either one
