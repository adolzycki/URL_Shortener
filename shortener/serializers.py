from rest_framework import serializers

from shortener.models import ShortendURL


class ShortendURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortendURL
        fields = ("short_url", "full_url")
        read_only_fields = ("short_url",)
