from django.contrib import admin
from .models import Activity


class ActivitiesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Activity, ActivitiesAdmin, name="Activities")
