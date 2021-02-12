import redis
import typing

class RedisBackend():
    
    def __init__(self, host: str, port: int, password: typing.Optional[str]):
        self._host = host
        self._port = port
        self._password = password
        self._redis = redis.Redis(self._host, self._port, 0, self._password)

    def setHost(self, hostname: str, ip: str, expireTime: int):
        try:
            self._redis.hset(hostname, "ip", ip)
            self._redis.expire(hostname, expireTime)
        except Exception as e:
            raise e

    def getIP(self, hostname: str) -> str:
        try:
            return self._redis.hget(hostname, "ip")
        except Exception as e:
            raise e