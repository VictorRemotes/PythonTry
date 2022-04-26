import csv
import datetime
import os

import loguru
from ProxiesFromProxyNova import getProxiesFromProxyNova

now = datetime.datetime.now()

proxies = []


def reqProxies(hour):
    global proxies
    proxies = proxies +getProxiesFromProxyNova()
    