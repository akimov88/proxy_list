from django.contrib import admin
from proxy_server.models import ProxyServer


@admin.register(ProxyServer)
class ProxyServerAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'updated',
        'name',
        'ip',
        'port',
        'proxy_type',
        'login',
        'password',
        'country',
        'available',
        'active',
    )
