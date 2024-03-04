from rest_framework.serializers import ModelSerializer
from proxy_server.models import ProxyServer


class ProxyServerSerializer(ModelSerializer):
    class Meta:
        model = ProxyServer
        fields = (
            'name',
            'address',
            'port',
            'proxy_type',
            'country',
            'is_available',
            'is_active',
        )
