from rest_framework.serializers import ModelSerializer
from proxy_server.models import ProxyServer


class ProxyServerSerializer(ModelSerializer):
    class Meta:
        model = ProxyServer
        fields = (
            'name',
            'ip',
            'port',
            'proxy_type',
            'country',
            'available',
            'active',
        )
