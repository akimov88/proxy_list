from django.db import models

from proxy_server.base.base_models import TimestampModel, TypeChoices


class ProxyServer(TimestampModel):
    ip = models.CharField(verbose_name='IP-адрес сервера', max_length=64)
    port = models.PositiveIntegerField(verbose_name='TCP/IP-порт сервера (1025..65635)')
    proxy_type = models.CharField(choices=TypeChoices.choices, default=TypeChoices.HTTP, max_length=64)
    login = models.CharField(verbose_name='Логин', max_length=256)
    password = models.CharField(verbose_name='Пароль', max_length=256)
    country = models.CharField(verbose_name='Страна', max_length=256)
    available = models.BooleanField(verbose_name='Доступность')

    class Meta:
        verbose_name = 'Прокси сервер'
        verbose_name_plural = 'Прокси серверы'
