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

loginname = '3414018462@qq.com'
password = 'qikuedu9527'

def login():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get('http://www.weibo.com/login.php')
        time.sleep(2)
        print('输入用户名...')
        elem_user = driver.find_element_by_id('loginname')
        elem_user.clear()
        elem_user.send_keys(loginname)
        time.sleep(3)
        print('输入密码...')
        elem_pwd = driver.find_element_by_name('password')
        elem_pwd.clear()
        elem_pwd.send_keys(password)
        time.sleep(3)
        print('点击登陆...')
        submit_btn = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
        submit_btn.click()
        time.sleep(10)
        print(driver.current_url)
        driver.close()

    except  Exception as e:
        print('登陆失败...')


if __name__ == '__main__':
    login()



