import time

import js2py
import loguru
import pyquery
import requests


def getProxiesFromProxyNova():
    proxies = []

    countries = [
        'tw',
        'jp',
        'kr',
        'id',
        'my',
        'th',
        'vn',
        'ph',
        'hk',
        'uk',
        'us'
    ]
    for country in countries:
        url = f'https://www.proxynova.com/proxy-server-list/country-{country}/'
        loguru.logger.debug(f'getProxiesFromProxyNova: {url}')
        loguru.logger.warning(f'getProxiesFromProxyNova: downloading...')
        response = requests.get(url)
        if response.status_code != 200:
            loguru.logger.debug(
                f'getProxiesFromProxyNova: status code is not 200')

            continue
        loguru.logger.success(f'getProxiesFromProxyNova: downloaded.')
        d = pyquery.PyQuery(response.text)
        table = d('table#tbl_proxy_list')
        rows = list(table('tbody:first > tr'))
        loguru.logger.warning(f'getProxiesFromProxyNova: scanning...')
        for row in rows:
            tds = list(row('td').items())

            if len(tds) == 1:
                continue

        js = row('td:nth-child(1) > addr').text()

        js = 'let x = %s; x' % (js[15:-2])

        ip = js2py.eval_js(js).strip()

        port = row('td:nth-child(2)').text().strip()

        proxy = f'{ip}:{port}'
        proxies.append(proxy)
    loguru.logger.success(f'getProxiesFromProxyNova: scanned')
    loguru.logger.debug(
        f'getProxiesFromProxyNova: {len(proxies)} proxies is found. ')

    time.sleep(1)

    return proxies
getProxiesFromProxyNova()