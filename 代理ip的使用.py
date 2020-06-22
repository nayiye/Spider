#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

import requests
from lxml import etree
import time
import random
import hashlib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def down(url,params=None):
    orderno = "ZF201910273585ew6xSN" # 订单号，替换
    secret = "1219111fc423464f9f1d3fde3ae6856a"  # 秘钥
    ip = "forward.xdaili.cn"
    port = "80"
    ip_port = ip + ":" + port
    nums = 1
    while nums<=3:
        timestamp = str(int(time.time()))
        string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp
        string = string.encode()
        md5_string = hashlib.md5(string).hexdigest()
        sign = md5_string.upper()
        auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp
        proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}

        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
            "Proxy-Authorization": auth,
        }
        try:
            response = requests.get(url, params=params,headers=headers, proxies=proxy, verify=False,allow_redirects=False)
            if response.status_code == 200:
                return response
            else:
                nums+=1
        except Exception as e:
            nums += 1
    return None

if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    response = down(url)
    if response != None:
        html = response.content.decode('utf-8')
        print(html)
