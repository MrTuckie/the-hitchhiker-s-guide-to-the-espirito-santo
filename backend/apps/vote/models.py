from django.contrib.auth.models import User
from django.db import models
from apps.post.models import Post


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    upvote = models.BooleanField(
        "Upvote",
        default=True,  # type: ignore
    )

    def __str__(self):
        upvote = "Upvote" if self.upvote else "Downvote"
        return f"A {upvote} from f{self.user} about {self.post}"
