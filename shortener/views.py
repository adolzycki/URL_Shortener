from secrets import token_urlsafe

from django.db import DataError, IntegrityError
from django.http import HttpResponseRedirect
from rest_framework import mixins, serializers, viewsets

from shortener.models import ShortendURL
from shortener.serializers import ShortendURLSerializer


class ShortendURLView(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = ShortendURL.objects.all()
    serializer_class = ShortendURLSerializer
    lookup_field = "short_url"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        full_url = instance.full_url
        return HttpResponseRedirect(full_url)

    def perform_create(self, serializer):
        for i in range(5):
            try:
                # Same url as an existing one may be randomly selected
                short_url = token_urlsafe(6)
                serializer.save(short_url=short_url)
            except (IntegrityError, DataError):
                continue
            else:
                return
        raise serializers.ValidationError("This url cannot be shortened.")
