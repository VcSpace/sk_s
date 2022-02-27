import os
import time
import threading
import keyboard

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from config import m_con, get_random_useragent
from datetime import datetime



"""
https://h5.stararknft.art/#/newBlindBox?id=10675&isbox=1
"""
def key_input4():
    while True:
        keyboard.wait('alt+a')
        print('alt+aaa 支付确定')
        try:
            browser.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/div[4]/div/div[2]/span[2]").click()  # 购买按钮2
        except:
            pass

def key_input3():
    while True:
        keyboard.wait('alt+r')
        print('alt+rrr 刷新')
        try:
            browser.get(m_con.buytarget)
        except:
            pass

def key_input2():
    while True:
        keyboard.wait('alt+d')
        print('alt+ddd 秒杀 支付密码+确定')
        try:
            browser.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/div[4]/div/div[1]/input").send_keys(m_con.payword)
            time.sleep(0.1)
            browser.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/div[4]/div/div[2]/span[2]").click()  # 购买按钮2
        except:
            pass

def key_input():
    while True:
        keyboard.wait('alt+q')
        print('alt+qqq 完整')
        try:
            browser.find_element(By.XPATH, "/html/body/div/div[1]/div[5]/button").click()  # 购买按钮
            time.sleep(0.2)
            browser.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/div[2]/div/span").click()  # 购买按钮2
            time.sleep(0.1)
            browser.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/div[4]/div/div[1]/input").send_keys(
                m_con.payword)
            time.sleep(0.1)
            browser.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/div[4]/div/div[2]/span[2]").click()  # 购买按钮2
        except:
            pass


def setdriver():
    moptions = webdriver.ChromeOptions()

    # 打开网页
    chrome_ua = get_random_useragent()

    print(m_con.buytarget)
    # moptions.add_argument(chrome_ua)
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
    return browser


browser = setdriver()

if __name__ == '__main__':
    print('Start')

    keyin = threading.Thread(target=key_input)  #
    keyin2 = threading.Thread(target=key_input2)
    keyin3 = threading.Thread(target=key_input3)
    keyin4 = threading.Thread(target=key_input4)


    keyin.start()
    keyin2.start()
    keyin3.start()
    keyin4.start()


    browser.get(m_con.loginurl) #未登录自动跳转到登录
    time.sleep(2)
    browser.refresh()  # 刷新方法 refresh
    browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/input").send_keys(m_con.username)
    browser.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/input").send_keys(m_con.password)
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/div/div[1]/span").click() #登录成功
    time.sleep(2)

    start_time = datetime.strptime('2022-02-27 19:59:59.800', "%Y-%m-%d %H:%M:%S.%f")
    now_time = datetime.now

    print('目标地址：', m_con.buytarget)
    print('开始时间: ', start_time)

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



    keyin.join()
    keyin2.join()
    keyin3.join()
    keyin4.join()

