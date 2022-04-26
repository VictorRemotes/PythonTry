import datetime

import chardet
import loguru
import pyquery
import requests


def main():

    resp = requests.get('https://www.taifex.com.tw/cht/9/futuresQADetail')
    
    if resp.status_code != 200:
        loguru.logger.error('RESP: status code is nnot 200')

    loguru.logger.success('RESP: success')

    txt = None
    det = chardet.detect(resp.content)
    try:
        if det['confidence'] > 0.5:
            if det['encoding'] == 'big-5':

                txt = resp.content.decode('big5')
            else:
                txt = resp.content.decode('utf-8')
    except Exception as e:
        loguru.logger.error(e)
        
    if txt is None:
        return
    
    loguru.logger.info(txt)
    

    if __name__ == '_main_':
        loguru.logger.add(
            f'datetime.date.today():%Y%m%d.log',
            rotation='1 day',
            retention='7 day',
            level='DEBUG'
        )


main()
