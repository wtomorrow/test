#！/user/bin/python
#-*-coding:utf-8-*-
import pytest,yaml
from appium import webdriver
from time import sleep


@pytest.fixture(scope="module")
def lian():
    d={
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "emulator-5554",
    "appPackage": "com.tencent.mobileqq",
    "appActivity": ".activity.SplashActivity",
    "noReset": "true"
    }
#建立连接并开启QQ程序
    dr=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=d)
#等待程序启动
    sleep(10)
    return dr




