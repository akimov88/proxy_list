from django.contrib import admin
from proxy_server.models import ProxyServer


@admin.register(ProxyServer)
class ProxyServerAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'updated',
        'name',
        'address',
        'port',
        'proxy_type',
        'username',
        'password',
        'country',
        'is_available',
        'is_active',
    )
