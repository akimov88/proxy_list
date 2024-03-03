from django.db import models


class TimestampModel(models.Model):
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        abstract = True


class TypeChoices(models.TextChoices):
    FTP = ('FTP', 'ftp')
    CGI = ('CGI', 'cgi')
    MAIL = ('SMPT, POP3, IMAP', 'smtp, pop3, imap')
    HTTP = ('HTTP, HTTPS', 'http, https')
    SOCKS = ('SOCKS', 'socks')


class CountryChoices(models.TextChoices):
    RU = ('RU', 'ru')
    US = ('US', 'us')
    UK = ('UK', 'uk')
    CN = ('CN', 'cn')
    CA = ('CA', 'ca')
    EU = ('EU', 'eu')
    AU = ('AU', 'au')
