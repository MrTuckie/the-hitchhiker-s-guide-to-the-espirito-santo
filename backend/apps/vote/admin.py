from django.contrib import admin

from apps.vote.models import Vote


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
