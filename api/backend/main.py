import fastapi
import os
import time
from typing import Optional
from redis_interface import RedisBackend

app = fastapi.FastAPI()
redis = RedisBackend(os.environ["REDIS_HOST"], int(os.environ["REDIS_PORT"]), os.environ["REDIS_PASS"])

SOA_FQDN = "13.113.130.62.xip.io"
DOMAIN_RNAME = "seolha314.gmail.com"

@app.get("/")
def default():
    return {"HI": "Working"}

@app.get("/dnsapi/lookup/{qname}/{qtype}")
def lookupDNS(qname: str, qtype: str, q: Optional[str] = None):
    hostname = extractHostname(qname)
    responseContent = {}
    responseContent["qtype"] = qtype
    responseContent["qname"] = qname[:-1]
    responseContent["ttl"] = 60
    if qtype == "SOA":
        responseContent["content"] = f"{SOA_FQDN}. {DOMAIN_RNAME}. {int(time.time())} 1800 3600 7200 5"
    elif qtype == "NS":
        responseContent["content"] = f"{SOA_FQDN}"
    elif qtype in ["A", "AAAA", "ANY"]:
        responseContent["content"] = redis.getIP(hostname)
    else:
        raise NotImplementedError
    return responseContent

@app.get("/dnsapi/lookup/{name}/{kind}")
def getDomainMetadata(name: str, kind: str, q: Optional[str] = None):
    return {"result": False}

def extractHostname(url: str):
    hostname = url[:-len(SOA_FQDN) - 1]
    if hostname == "":
        raise NameError
    else:
        return hostname