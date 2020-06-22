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
from selenium.webdriver.common.by import By # 定位条件
from selenium.webdriver.support.ui import WebDriverWait  # 智能等待对象
from selenium.webdriver.support import expected_conditions  as EC  # 设定加载条件
from selenium.common.exceptions import TimeoutException # 超时的异常
from selenium.webdriver.common.action_chains import ActionChains # 动作练
import time
import random
import re

browser = webdriver.Chrome()
browser.maximize_window()
wait = WebDriverWait(browser,60)

try:
    browser.get('https://www.taobao.com/')
    print('定位输入框...')
    # 定位输入框
    tb_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#q'))
    )
    print('定位搜索按钮...')
    # 定位搜索按钮
    search_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn-search.tb-bg'))
    )
    tb_input.send_keys('移动硬盘')
    print('搜索...')
    search_btn.click()
    ls = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist'))
    )
    # 定位总的页数
    total = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.total'))
    )

    while True:
        # 定位商品的条目
        ls = wait.until(
           EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class,"item J_MouserOnverReq")]'))
        )
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(random.random()*2)
        print('len:',len(ls))
        for item in ls:
            title = item.find_elements_by_xpath('.//div[@class="row row-2 title"]/a')[0].text.strip()
            print('title:',title)
            price = item.find_elements_by_xpath('.//div[@class="price g_price g_price-highlight"]/strong')[0].text.strip()
            print('price:',price)
            print('='*600)

        browser.execute_script('window.scrollTo(0,document.body.scrollHeight-500);')
        # 翻页按钮
        next_page_btn = wait.until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="J_Ajax num icon-tag"]'))
        )
        print('开始翻页...')
        action = ActionChains(browser)
        action.move_to_element(next_page_btn).click().perform()
        time.sleep(random.random()*5)

except TimeoutException as e:
    print(e)


#browser.quit()









