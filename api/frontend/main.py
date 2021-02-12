import fastapi
import os
import re
from typing import Optional
from redis_interface import RedisBackend

app = fastapi.FastAPI()
redis = RedisBackend(os.environ["REDIS_HOST"], int(os.environ["REDIS_PORT"]), os.environ["REDIS_PASS"])

@app.get("/")
def test_root():
    return {"This is a": "TEST"}

@app.get("/set/{host}/{ip}")
def set_host(host: str, ip: str, q: Optional[str] = None):
    redis.setHost(host, ip, 30 * 86400)
    return {"Result": "OK"}

@app.get("/get/{host}")
def get_host(host: str, q: Optional[str] = None):
    ip = redis.getIP(host)
    return {"IP": str(ip)}