import re
from sre_constants import SUCCESS
import time
from urllib import response
import urllib.parse

import json
import loguru
import pyquery
import requests

def getProxiesFromGatherProxy():
    proxies = []
    
    countries = [
        'Taiwan',
        'Japan',
        'United States',
        'Thailand',
        'Vietnam',
        'Indonesia',
        'Singapore',
        'Philippines',
        'Malaysia',
        'Hong Kong'
    ]
    for country in countries:
        url = f'http://www.gatherproxy.com/proxylist/country/?c={urllib.parse.quote(country)}'
        loguru.logger.debug(f'getProxiesFromGatherProxy;{url}')
        loguru.logger.warning(f'getProxiesFromGatherProxy: downloading...')
        response = requests.get(url)
        
        if response.status_code != 200:
            loguru.logger.debug(f'getProxiesFromGatherProxy: status code is not 200')
            
            continue
        
        loguru.logger.success(f'getProxiesFromGatherProxy: downloaded.')

        d=pyquery.PyQuery(response.text)
        scripts = list(d('table#tblproxy > script').items())
        loguru.logger.warning(f'getProxiesFromGatherProxy: scanning...')
        for script in scripts:
            
            script = script.text().strip()
            
            
        
            

