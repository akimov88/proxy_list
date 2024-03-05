from logging import Logger

from celery import shared_task

from proxy_server.models import ProxyServer
from proxy_server.services import ContextManager

logger = Logger('proxy_server.tasks')


@shared_task
def check_proxy_server_task(id: int) -> None:
    p = ProxyServer.objects.get(id=id)
    with ContextManager(address=p.address, port=p.port) as context:
        p.is_available = context.check_host()
        p.is_active = context.request_by_proxy()
        p.country = context.host_info.get('countryCode')
        p.save()
