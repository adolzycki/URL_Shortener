from rest_framework.routers import DefaultRouter

from shortener.views import ShortendURLView

router = DefaultRouter()

router.register(r"", ShortendURLView, basename="")

urlpatterns = router.urls
