import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from config import m_con, get_random_useragent
from datetime import datetime



"""
https://h5.stararknft.art/#/newBlindBox?id=10675&isbox=1
"""

if __name__ == '__main__':
    print('Start')


    moptions = webdriver.ChromeOptions()

    # 打开网页
    chrome_ua = get_random_useragent()

    print(m_con.buytarget)
    moptions.add_argument(chrome_ua)
    moptions.add_argument('--disable-gpu')
    moptions.add_argument('blink-settings=imagesEnabled=false') #禁用图片
    #最高权限
    moptions.add_argument('--no-sandbox')
    moptions.add_argument('--window-size=1548,900')
    # 设置浏览器以无界面方式运行
    #options.add_argument('--headless')

    # 禁用浏览器弹窗
    # prefs = {
    #     'profile.default_content_setting_values' :  {
    #         'notifications' : 2
    #      }
    # }
    # moptions.add_experimental_option('prefs',prefs)

    browser = webdriver.Chrome(options=moptions)
    """
    ----------------------------------------------
    """


    browser.get(m_con.loginurl) #未登录自动跳转到登录
    time.sleep(2)
    browser.refresh()  # 刷新方法 refresh
    browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/input").send_keys(m_con.username)
    browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/input").send_keys(m_con.password)
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/div/div[1]/span").click() #登录成功
    time.sleep(2)

    start_time = datetime.strptime('2022-02-27 19:59:59.850', "%Y-%m-%d %H:%M:%S.%f")
    now_time = datetime.now

    while True:
        if now_time() >= start_time:
            try:
                browser.get(m_con.buytarget)
                time.sleep(0.2)
                browser.find_element(By.XPATH, "/html/body/div/div[1]/div[5]/button").click() #购买按钮
                time.sleep(0.2)
                browser.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/div[2]/div/span").click() #购买按钮2
                time.sleep(0.2)
                browser.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/div[4]/div/div[1]/input").send_keys(m_con.payword)
                time.sleep(0.1)
                browser.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/div[4]/div/div[2]/span[2]").click() #购买按钮2
            except:
                pass
            break
        else:
            time.sleep(0.1)
            print('sleep 0.1')
