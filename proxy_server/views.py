from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

from proxy_server.models import ProxyServer
from proxy_server.serializers import ProxyServerSerializer


class ProxyServerViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = ProxyServer.objects.all()
    serializer_class = ProxyServerSerializer
