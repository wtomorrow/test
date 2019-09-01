#！/user/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
from time import sleep
import yaml,pytest
from until.xxxx import s
from until.mylog import get_logger
log = get_logger(filename="test.py")



# 建立连接并开启QQ
with open(file=r"E:\QQ\element\login.yaml",mode='r',encoding="utf-8")as fb:
    e=yaml.load(fb,Loader=yaml.FullLoader)
    print(e)

# def test_1(lian):
#     lian.find_element_by_xpath(e['tou']).click()
#     sleep(2)
#     lian.find_element_by_id(e['seting']).click()
#     sleep(2)
#     lian.find_element_by_id(e['zhanghao']).click()
#     sleep(3)
#     lian.find_element_by_id(e['tuihao']).click()
#     sleep(2)
#     lian.find_element_by_id(e['tuichu']).click()
#     sleep(2)
#     lian.find_element_by_id(e['quxiao']).click()
#     sleep(10)
#     text=lian.find_element_by_accessibility_id(e['duanyan']).text
#     assert text == "用户注册"

@pytest.mark.parametrize("zh,mi",s)
def test_2(lian,zh,mi):
    #先清除之前的数据
    lian.find_element_by_xpath(e['hhh']).clear()
    sleep(5)
    #在向账号框中输入账号
    # log.info(f"zhanghao是{zh},mima是{mi}")
    lian.find_element_by_xpath(e['hhh']).send_keys(zh)
    sleep(3)
    lian.find_element_by_id(e['mima']).clear()
    #输入密码
    lian.find_element_by_id(e['mima']).send_keys(mi)
    sleep(3)
    #点击登录
    lian.find_element_by_id(e['deng']).click()
    sleep(5)
    # try:
    #     text=lian.find_element_by_accessibility_id(e["xinynghu"])
    #     assert text =="用户注册"
    # except:
    #     text = lian.find_element_by_accessibility_id(e["xinyonghu"])
    #     assert text == "确定"
    # try:
    #     text = lian.find_element_by_accessibility_id(e["xinyonghu"])
    #     assert text == "消息"
    # except:






