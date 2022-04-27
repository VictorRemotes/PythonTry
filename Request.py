import loguru
import requests
import requests.exceptions
import ProxyList


proxy = None

def testRequests():
    global proxy
    
    while True:
        
        if proxy is None:
            proxy = ProxyList.getProxy()
        try:
            url = f'https://www.google.com'
            loguru.logger.info(f'testRequest: url is {url}')
            loguru.logger.warning(f'testRequest: downloading...')
            response = requests.get(
                url,
                
                proxies={
                    'http': f'https://{proxy}'
                },
                timeout=5
            )
            
            if response.status_code !=200:
                loguru.logger.debug(f'testRequest: status code is not 200.')
                
                proxy = None
                continue
            loguru.logger.success(f'testReqest: downloaded.')
            
        except requests.exceptions.ConnectionError:
            loguru.logger.error(f'testRequest: proxy({proxy}) is not working (connection error).')
            proxy = None
            continue
        except requests.exceptions.ConnectTimeout:
            loguru.logger.error(f'testRequest: proxy({proxy}) is not working (connect timeout).')
            proxy = None
            continue
        except requests.exceptions.ProxyError:
            loguru.logger.error(f'testRequest: proxy({proxy}) is not working (proxy error).')
            proxy = None
            continue
        except requests.exceptions.SSLError:
            loguru.logger.error(f'testRequest: proxy({proxy}) is not working (ssl error).')
            proxy = None
            continue
        except Exception as e:
            loguru.logger.error(f'testRequest: proxy({proxy}) is not working.')
            loguru.logger.error(e)
            proxy = None
            continue
        # 成功完成請求，離開迴圈
        break
testRequests()
