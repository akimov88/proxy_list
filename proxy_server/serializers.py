from rest_framework.serializers import ModelSerializer
from proxy_server.models import ProxyServer


class ProxyServerSerializer(ModelSerializer):
    class Meta:
        model = ProxyServer
        fields = (
            'name',
            'address',
            'port',
            'type',
            'country_code',
            'is_active',
            'is_available',
        )
