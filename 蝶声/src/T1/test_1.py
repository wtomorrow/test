#！/user/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
from until.滑动 import hh_up
from time import sleep
import yaml,pytest
from until.jiaoben import s
#建立连接并开启蝶声
with open(file=r"E:\蝶声\element\login.yaml",mode='r',encoding="utf-8") as f:
    l = yaml.load(f, Loader=yaml.FullLoader)
    print(l)

@pytest.mark.parametrize("za,mm",s)
def test_1(foo,za,mm):
    #先清除之前的数据
    foo.find_element_by_id(l['zhanghao']).clear()
    sleep(5)
    #在向账号框中输入账号
    foo.find_element_by_id(l['zhanghao']).send_keys(za)
    sleep(3)
    # 先清除之前的数据
    foo.find_element_by_id(l['mima']).clear()
    sleep(4)
    #输入密码
    foo.find_element_by_id(l['mima']).send_keys(mm)
    sleep(3)
    #点击登录
    foo.find_element_by_id(l['deng']).click()
    sleep(5)
    #断言
    try:
        q=foo.find_element_by_id(l["duan"]).text
        assert q == "直播"
        log.info('登录成功')
    except:
        w=foo.find_element_by_id(l['yan']).text
        assert w=="忘记密码"
        log.info('登录失败')




""""
#滑动
def test_2(foo):
    #向上滑动
    hh_up(foo)
    sleep(10)

#退出登录
def test_3(foo):
    #点击我的
    foo.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
    sleep(8)
    #向上滑动
    hh_up(foo)
    sleep(4)
    #点击设置
    foo.find_element_by_id(l['she']).click()
    sleep(6)
    #点击退出
    foo.find_element_by_id(l['tui']).click()
    sleep(5)
    #单击确定
    foo.find_element_by_id(l['hoo']).click()
    sleep(10)

# 编辑昵称
def test_4(foo):
    #点击我的
    foo.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
    sleep(8)
    #点击编辑资料
    foo.find_element_by_id(l['bianji']).click()
    sleep(5)
    #点击昵称
    foo.find_element_by_id(l['nicheng']).click()
    sleep(3)
    #清楚昵称框
    foo.find_element_by_id(l['nn']).clear()
    sleep(5)
    #编写昵称
    foo.find_element_by_id(l['nn']).send_keys('wiueiuu')
    sleep(6)
    #点击保存
    foo.find_element_by_id(l['baocun']).click()
    sleep(6)

#编辑性别
def test_5(foo):
    #点击我的
    foo.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
    sleep(8)
    #点击编辑资料
    foo.find_element_by_id(l['bianxie']).click()
    sleep(6)
    #点击性别
    foo.find_element_by_id(l['sex']).click()
    sleep(5)
    #选择性别
    foo.find_element_by_id('com.qk.butterfly:id/v_list').find_element_by_class_name('android.widget.LinearLayout')[-2].click()
    sleep(6)
    #点击保存
    foo.find_element_by_id(l['bb']).click()
    sleep(5)

#编辑个性签名
def test_6(foo):
    #单击我的
    foo.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
    #单击编辑资料
    foo.find_element_by_id('bianb').click()
    sleep(3)
    #点击个性签名
    foo.find_element_by_id('qian').click()
    sleep(3)
    #写
    foo.find_element_by_id('xie').send_keys('青山不及你眉长')
    sleep(5)
    #单击返回
    foo.find_element_by_id('fan').click()
    sleep(2)
    #单击保存
    foo.find_element_by_id('cun').click()
    sleep(3)

"""













