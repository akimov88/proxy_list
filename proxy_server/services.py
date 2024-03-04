import requests


class ContextManager:
    def __init__(self, address: str = 'x.agava.space', port: int = 58772):
        self.__address = address
        self.__port = port
        self.__host_data = {}

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    @property
    def host(self) -> str:
        return f'{self.__address}:{self.__port}'

    @property
    def host_info(self):
        if not self.__host_data:
            self.check_host()
        return self.__host_data

    def check_host(self) -> bool:
        r = requests.get(url=f'http://ip-api.com/json/{self.__address}')
        self.__host_data = r.json()
        return r.ok

    def request_by_proxy(self, url: str = 'https://google.com') -> bool:
        r = requests.get(url=url, proxies={'http': f'{self.__address}:{self.__port}'})
        return r.ok
