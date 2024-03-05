from django.db import models

from proxy_server.base.base_models import TimestampModel, ProxyTypes
from proxy_server.tasks import check_proxy_server_task


class ProxyServer(TimestampModel):
    name = models.CharField('Имя хоста', max_length=256)
    address = models.CharField('Адрес хоста', max_length=256)
    port = models.PositiveIntegerField('TCP/IP-порт хоста (1025..65635)')
    proxy_type = models.CharField('Тип', choices=ProxyTypes.choices, default=ProxyTypes.HTTP, max_length=64)
    username = models.CharField('Логин', max_length=256, blank=True, null=True)
    password = models.CharField('Пароль', max_length=256, blank=True, null=True)
    country = models.CharField('Код страны', max_length=2, blank=True, null=True)
    is_active = models.BooleanField('Активен', default=False)
    is_available = models.BooleanField('Доступен', default=False)

    class Meta:
        verbose_name = 'Прокси сервер'
        verbose_name_plural = 'Прокси серверы'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        check_proxy_server_task.delay(self)
