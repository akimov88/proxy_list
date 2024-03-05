from logging import Logger

from celery import shared_task

from proxy_server.services import ContextManager

logger = Logger('proxy_server.tasks')


@shared_task
def check_proxy_server_task(server) -> None:
    with ContextManager(address=server.address, port=server.port) as context:
        server.is_available = context.check_host()
        server.is_active = context.request_by_proxy()
        server.country = context.host_info.get('countryCode')
    server.save()
