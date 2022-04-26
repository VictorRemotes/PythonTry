import datetime
from email import message
import imp
import os

import chardet
import loguru
import pyquery
import requests
from Propotion import Propotion


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
    # 成分股市值佔比清單
    proportions = []

    # 將下載回來的內容解析為 PyQuery 物件
    d = pyquery.PyQuery(txt)

    # 透過 CSS 選擇器取出所有表格行
    trs = list(d('table tr').items())

    # 去除標頭行（分析結果 1.）
    trs = trs[1:]

    # 依序取出資料行
    for tr in trs:

        tds = list(tr('td').items())

        code = tds[1].text().strip()

        if code != '':
            sort = tds[1].text().strip()
            name = tds[2].text().strip()
            percent = tds[3].text().strip()

            proportions.append(Propotion(
                sort=sort,
                code=code,
                name=name,
                percent=percent
            ))

        code = tds[5].text().strip()

        if code != '':

            sort = tds[5].text().strip()

            name = tds[6].text().strip()

            percent = tds[7].text().strip()

            proportions.append(Propotion(
                sort=sort,
                code=code,
                name=name,
                percent=percent
            ))

        proportions.sort(key=lambda proportion: proportion.Code)
        loguru.logger.info(proportions)

        message = os.linesep.join([str(proportion)
                                  for proportion in proportions])
        
        loguru.logger.info('PROPORTIONS' + os.linesep + message)

    if __name__ == '_main_':
        loguru.logger.add(
            f'datetime.date.today():%Y%m%d.log',
            rotation='1 day',
            retention='7 day',
            level='DEBUG'
        )


main()
