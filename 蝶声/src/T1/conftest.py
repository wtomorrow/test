#！/user/bin/python
#-*-coding:utf-8-*-
import pytest,yaml
from appium import webdriver
from time import sleep


@pytest.fixture(scope="module")
def foo():
    d={
    "platformName": "Android",   #  系统类型
    "platformVersion": "5.1.1",  #系统版本
    "deviceName": "emulator-5554",#  手机序列
    "appPackage": "com.qk.butterfly",# 安装包名
    "appActivity": ".main.LauncherActivity",# 活动栈
    "noReset": "true"
    }

    # 建立连接并开启蝶声程序
    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
    # 等待程序启动
    sleep(10)
    dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
    sleep(10)
    return dr