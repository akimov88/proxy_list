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
        'type',
        'username',
        'password',
        'country_code',
        'is_active',
        'is_available',
    )
