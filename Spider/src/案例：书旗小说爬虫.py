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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # 智能等待对象
from selenium.webdriver.support import expected_conditions as EC  # 等待加载的条件

import time
import random

url = 'http://t.shuqi.com/route.php?#!/bid/6813921/cid/678442/ct/read'

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,30)
driver.get(url)

for page in range(10):
    try:
        # 等待
        con_texts = wait.until(
            EC.presence_of_all_elements_located((By.XPATH,'//div[@class="read-body"]/div'))
        )
        time.sleep(5)
        # 关闭向导
        tips = driver.find_elements_by_xpath('//div[@class="tips_gesture tips_lr"]')
        if len(tips) > 0:
            tips[0].click()
        # 关闭广告
        ad_close_btn = driver.find_elements_by_xpath('//i[@class="ico-promo-close"]')
        if len(ad_close_btn)>0:
            ad_close_btn[0].click()

        print('len:', len(con_texts))
        # 数据提取
        title = driver.find_elements_by_xpath('//div[@class="read-body"]/div/h3')[0].text
        print('title:',title)
        # 显示小说内容
        myjs = '''
        elems = document.querySelectorAll("div.read-body div");
        for(var i=0;i<elems.length;i++){
            elems[i].style.display="block";
        }    
        '''
        driver.execute_script(myjs)
        # 提取章节内容
        con_texts = driver.find_elements_by_xpath('//div[@class="read-body"]/div/p')
        con_texts = ["\n    "+elem.text for elem in con_texts]
        con_texts = ''.join(con_texts)
        print('content:',con_texts)
        # 显示翻页导航工具
        myjs ='''
        var x = document.getElementsByClassName("js-read-bottom");
        x[0].setAttribute('class',"readbottom-box js-read-bottom js-read-set");
        '''
        driver.execute_script(myjs)
        next_btn = driver.find_elements_by_xpath('//div[@class="next"]')
        if len(next_btn)>0:
            next_btn[0].click()
        else:
            break
    except Exception as e:
        print('error',e)

print('over....')








