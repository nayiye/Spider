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
import time
import random

url = 'https://www.jd.com/'

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(url)
time.sleep(2)
print('输入搜索的商品：')
tb_input = driver.find_element_by_id("key")
search_btn = driver.find_element_by_css_selector('.button')
tb_input.send_keys('无人机')
time.sleep(2)
search_btn.click()
time.sleep(2)

for page in range(5):
    # 把滚动条模拟拖动到浏览器底部
    for i in range(3):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(random.random()*2)

    goods_ls = driver.find_elements_by_css_selector('.gl-item')
    print('goods len:',len(goods_ls))
    for info in goods_ls:
        title = info.find_element_by_css_selector('.p-name.p-name-type-2 a').text.strip()
        print('title:',title)
        price = info.find_element_by_css_selector('.p-price').text.strip()
        print('price:',price)
        print('='*600)

    print('next page...')
    next_btn = driver.find_elements_by_css_selector('a.pn-next')
    if len(next_btn)>0:
        next_btn=next_btn[0]
        next_btn.click()
    else:
        break

driver.close()






