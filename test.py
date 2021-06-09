# -*- coding:UTF-8 -*-
import requests
import re
import base64
import time
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 获取详情页链接
    target = 'https://www.mattkaydiary.com/'
    req = requests.get(url=target)
    soup = BeautifulSoup(req.text, "html5lib").select('.post-title > a')
    link = soup[0].get('href')
    print(link)

    # 获取jd信息
    content = requests.get(url=link)
    pattern = r'([vmess|ss]{2,5}:\/\/[^<]{10,})'
    result = re.findall(pattern, content.text, re.M)

    # 写入文件
    result = '\n'.join(result)
    result = str(base64.b64encode(result.encode('utf-8')),"utf-8")
    filename = time.strftime("%Y-%m-%d", time.localtime())
    with open('otw/'+filename + '.txt', 'w') as f:
      f.write(result)