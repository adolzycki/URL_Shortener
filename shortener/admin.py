from django.contrib import admin

from shortener.models import ShortendURL


@admin.register(ShortendURL)
class ShortendURLAdmin(admin.ModelAdmin):
    list_display = (
        "short_url",
        "full_url",
    )
