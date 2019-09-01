#！/user/bin/python
#-*-coding:utf-8-*-
"""
appium的三种等待
1、sleep---->强制等待 工作的线程会停止一段时间
2、隐性等待---->implicity_wait(10)，设置最大等待时间，关键字参数：time_to_wait=10,超过最大等待时间后则抛出异常
3、安卓独有---->wait_activity():
等待某个activity出现，设置最大等待时间，超出最大等待时间，就会抛出异常（只能用于等待activity）
4、智能等待
locator = (By.ID, "android:id/tabs")
try:
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((locator))
except:

"""
#WebDriverWait---->等待某一个元素加载出来
#expected_conditions selenium 的异常处理类
#By ------>指通过什么方式进行定位
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

WebDriverWait("参数一","参数二","参数三").until(EC.presence_of_all_elements_located("参数四"))
"""
参数一：我们与手机建立的回话----->dr
参数二：最大等待时间，单位是秒
参数三：刷新页面的时间，间隔为多少，单位为秒
直到某个元素被找到，停止等待
until(EC.presence_of_all_elements_located("参数四")
参数四：一个由定位方法，和元素组成的元组   例如：(By.ID,"元素")
"""

















