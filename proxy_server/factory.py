import requests
import logging

from proxy_server.models import ProxyServer

logger = logging.Logger('proxy_server.factory')


class ClassNotFoundError(ValueError):
    pass


class NotAvailableProxyError(ValueError):
    pass


class ProxyFactoryObject(object):
    pass


class ProxySession(ProxyFactoryObject):
    def __init__(self):
        self.__server: (object, None) = None
        self.__session: (requests.Session, None) = None

    def __enter__(self):
        self.__server = ProxyServer.objects.filter(is_available=True).first()
        if self.__server:
            self.__server.is_available = False
            self.__server.save()
            self.__session = requests.Session()
        else:
            raise NotAvailableProxyError
        if all((self._check_host(), self._request_by_proxy())):
            return self.__session

    def __exit__(self, type, value, traceback):
        self.__server.is_available = True
        self.__server.save()
        self.__session = None

    def _check_host(self) -> bool:
        r = requests.get(url=f'http://ip-api.com/json/{self.__server.address}')
        r.raise_for_status()
        logger.info(msg=f'_check_host: {r}')
        return r.ok

    def _request_by_proxy(self, url: str = 'https://google.com') -> bool:
        proxies = {'http': f'{self.__server.address}:{self.__server.port}'}
        r = requests.get(url=url, proxies=proxies)
        if not r.raise_for_status():
            self.__session.proxies.update(proxies)
        logger.info(msg=f'_request_by_proxy: {r}')
        return r.ok

    @property
    def session(self) -> requests.Session:
        return self.__session


class ProxyFactory:
    @staticmethod
    def get(class_name: str):
        if not isinstance(class_name, str):
            raise ValueError('class_name must be a string')
        subclasses = ProxyFactoryObject.__subclasses__()
        class_dict = {c.__name__: c for c in subclasses}
        c = class_dict.get(class_name, None)
        if c is not None:
            return c
        raise ClassNotFoundError
