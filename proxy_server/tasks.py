from logging import Logger

from celery import shared_task

from proxy_server.models import ProxyServer

logger = Logger('proxy_server.tasks')
