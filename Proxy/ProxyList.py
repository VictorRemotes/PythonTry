import os
import csv
import loguru
import random
import datetime

from Proxy.ProxiesFromProxyNova import getProxiesFromProxyNova
from Proxy.ProxiesFromGatherProxy import getProxiesFromGatherProxy
from Proxy.ProxiesFromFreeProxyList import getProxiesFromFreeProxyList


now = datetime.datetime.now()
proxies = []

# 隨機取出一組代理
def getProxy():
    global proxies
    
    # 若代理清單內已無代理，則重新下載
    if len(proxies) == 0:
        getProxies()
    proxy = random.choice(proxies)
    loguru.logger.debug(f'getProxy: {proxy}')
    proxies.remove(proxy)
    loguru.logger.debug(f'getProxy: {len(proxies)} proxies is unused.')
    return proxy


# 取得模組執行當下時間
now = datetime.datetime.now()
# 透過全域變數共用代理清單
proxies = []

# 下載代理清單
def reqProxies(hour):
    global proxies
    proxies = proxies + getProxiesFromProxyNova()
    proxies = proxies + getProxiesFromGatherProxy()
    proxies = proxies + getProxiesFromFreeProxyList()
    
    loguru.logger.debug(f'reqProxies: {len(proxies)} proxies is found.')
    
# 取得代理清單
def getProxies():
    global proxies
    now = datetime
    hour = f'{now:%Y%m%d%H}'
    filename = f'proxies-{hour}.csv'
    filepath = f'{filename}'
    if os.path.isfile(filepath):
        # 如果本小時的紀錄檔案存在，直接載入代理清單
        loguru.logger.info(f'getProxies:{filename} exists')
        loguru.logger.warning(f'getProxies: {filename} is loading...')
        with open(filepath, 'r',newline='',encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                proxy = row['Proxy']
                proxies.append(proxy)
        loguru.logger.success(f'getProxies: {filename} is loaded')
    else:
        # 如果本小時的紀錄檔案存在，重新下載代理清單並保存
        loguru.loggerinfo(f'getProxies: {filename} does not exist.')
        reqProxies(hour)
        loguru.logger.warning(f'getProxies: {filename} is saving...')
        with open(filepath,'w',newline='',encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Proxy'
            ])
            for proxy in proxies:
                writer.writerow([
                    proxy
                ])
        loguru.logger.success(f'getProxies: {filename} is saved.')
        
        
        
        
    