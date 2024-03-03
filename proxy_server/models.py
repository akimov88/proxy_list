from django.db import models

from proxy_server.base.base_models import TimestampModel, TypeChoices


class ProxyServer(TimestampModel):
    name = models.CharField('Имя подключения', max_length=128)
    ip = models.GenericIPAddressField('IP-адрес сервера')
    port = models.PositiveIntegerField('TCP/IP-порт сервера (1025..65635)')
    proxy_type = models.CharField('Тип', choices=TypeChoices.choices, default=TypeChoices.HTTP, max_length=64)
    login = models.CharField('Логин', max_length=256)
    password = models.CharField('Пароль', max_length=256)
    country = models.CharField('Страна', max_length=256)
    available = models.BooleanField('Доступность')
    active = models.BooleanField('Активность')

    class Meta:
        verbose_name = 'Прокси сервер'
        verbose_name_plural = 'Прокси серверы'
