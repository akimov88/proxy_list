from rest_framework.routers import SimpleRouter

from proxy_server.views import ProxyServerViewSet

router = SimpleRouter(trailing_slash=False)
router.register(prefix='proxy_server', viewset=ProxyServerViewSet)
urlpatterns = router.urls
