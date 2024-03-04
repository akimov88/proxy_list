import requests


class ProxyContext:
    def __init__(self, address: str = 'x.agava.space', port: int = 58772):
        self.__address = address
        self.__port = port
        self.__resource = self

    def __enter__(self):
        return self.__resource

    def __exit__(self, type, value, traceback):
        self.__resource.post_work()

    @property
    def host(self):
        return f'{self.__address}:{self.__port}'

    def check_host(self):
        r = requests.get(url=f'http://ip-api.com/json/{self.__address}')
        return r.json()

    def proxy_request(self):
        r = requests.get(url='https://google.com', proxies={'http': f'{self.__address}:{self.__port}'})
        return r.ok

    def post_work(self):
        pass
