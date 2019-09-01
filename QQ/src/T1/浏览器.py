#！/user/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains

# 浏览器页面设置
"""
dr.get('http://www.jd.com')
sleep(5)
回到上次页面
dr.back()
前进到第二个页面
dr.forward()
获取访问网址的标题
dr.title
获取访问的网址
dr.current_url
设置浏览器窗口的大小
dr.set_window_size(400,600)
设置浏览器的位置
dr.set_window_position(500,700)
最大化浏览器
dr.maximize_window()
最小化浏览器
dr.minimize_window()
"""
#浏览器定位    核心：定位
"""
八种定位方法：1、ID；2、class；3、name；4、link_text；5、tag_name；6、xpath；7、css；8、partial_link_text

1、ID定位    动作：1、click()；2、send_keys('内容')
dr.find_element_by_id('kw').send_keys('python')

2、class定位
dr.find_element_by_class_name('class属性的值')

3、name  指得是name属性
dr.find_element_by_name('name属性的值')

4、link_text定位   文本定位
dr.find_element_by_link_text('新闻').click()

5、partial_link_text   模糊文本
dr.find_element_by_partial_link_text()

6、tag_name  标签定位：通常定位一组对象

7、xpath  路径标记语言：绝对路径、相对路径
   xml:可扩展标记语言  作用：用来储存数据
dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[1]')

8、css  层叠样式
dr.find_element_by_css_selector('a.mnav:nth-child(1)')

定位一组对象   （同时定位到多个元素,结果是个列表）
层级定位：先定义一个大的范围，再从大的范围中定位元素
dr.父元素.子元素.动作
父元素必须是唯一的，子元素可以是一组也可以是唯一的

例子
dr.get('https://www.ctrip.com')
sleep(3)
ww=dr.find_element_by_id("searchHotelLevelSelect").find_elements_by_tag_name("option")
for i in ww:
    i.click()
    sleep(2)
# print(len(ww))
定位文本元素
r=dr.find_element_by_id('J_roomCountList').find_elements_by_tag_name("option")
for j in r:
    j.click()
    sleep(3)
print(len(r))

dr.get('https://www.jd.com')
sleep(4)
#定位家用电器
q=dr.find_element_by_id('J_cate').find_elements_by_class_name('cate_menu_item')
sleep(3)
for i in q:
    print(i.text)
    sleep(3)
"""
# 处理框架
"""
iframe：内嵌框架；  switch_to：切换框架；  login_frame：框架名称；
切换框架时，只可以用id的值或name的值；
若没有id没有name的情况下，则先定位到框架，再用xpath切换
dr.switch_to.frame('login_frame')
sleep(3)
#退出到上一层框架
dr.switch_to.parent_frame('')
#退出到第一层页面
dr.switch_to_default.content('')
sleep(3)
"""

# 窗口处理
"""
#浏览器管理窗口的原理：
#浏览器会对每个打开的窗口生成一个唯一标识窗口的句柄
#谷歌产生的句柄是一堆字符串；火狐产生的是一堆数字
dr = webdriver.Firefox()
# # 访问网址
dr.get('https://www.douban.com/')
sleep(3)
#获取当前的窗口的句柄
dd=dr.current_window_handle
print(dd)
dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()
sleep(3)
# 获取所有窗口的句柄
dd=dr.window_handles
print(dd)
#切换窗口
dr.switch_to.window(dd[-1])
print(dr.title)
"""
# 处理弹出框
"""
dr = webdriver.Firefox()
dr.get("file:///C:/Users/huazheng/Documents/tencent%20files/1719652243/filerecv/abc.html")
sleep(3)
dr.find_element_by_xpath('/html/body/button').click()
sleep(3)
#处理弹出框  alter弹出框
#将鼠标切换到弹出框
ww=dr.switch_to_alert()
print(ww.text)                 #获取弹出框的文本
ww.send_keys("小可爱")        #弹出框上的输入内容
ww.accept()                    #点击弹出框上的确定
ww.dismiss()                  #点击弹出框上的取消
"""
#滚动条的操作
"""
执行Javascript函数
用法：1、滚动到指定位置；
dr = webdriver.Firefox()
dr.get('https://www.ifeng.com/')
sleep(4)
dd=dr.find_element_by_xpath('/html/body/div[1]/div/div[9]/div[2]/div[1]/div[1]/div[1]/a[1]')
sleep(5)
dr.execute_script("arguments[0].scrollIntoView();",dd)
2、页面的高度滑动滚动条   6000指的是高度
for i in range(0,6000,200):
    js=f"var q=document.documentElement.scrollTop={i}"
    dr.execute_script(js)
    sleep(2)
"""

#发邮件

dr = webdriver.Chrome()
#请求网址
dr.get("https://mail.qq.com")
sleep(3)
#设置框架
dr.switch_to.frame('login_frame')
sleep(2)
#点击账号密码登录
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(2)
#输入账号
dr.find_element_by_xpath('//*[@id="u"]').send_keys("1719652243")
sleep(2)
#输入密码
dr.find_element_by_xpath('//*[@id="p"]').send_keys('D.1996949')
sleep(2)
#点击登录
dr.find_element_by_id('login_button').click()
sleep(10)
#点击写信
dr.find_element_by_id('composebtn_td').click()
sleep(2)
#退出框架
# dr.switch_to.default_content()
# sleep(3)
#切换框架
dr.switch_to.frame('mainFrame')
sleep(2)
#点击收件人
dr.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('2573768362')
sleep(3)
#点击输入主题
dr.find_element_by_id('subject').send_keys("hello world")
sleep(5)
#定位
w=dr.find_element_by_class_name('qmEditorIfrmEditArea').click()
sleep(2)
#切换框架
dr.switch_to.frame(w)
sleep(2)
#点击输入正文
dr.find_element_by_xpath('/html/body').send_keys('小可爱很可爱')
sleep(3)
#退出框架
dr.switch_to.parent_frame()
sleep(3)
#切换框架
dr.switch_to.frame('mainFrame')
sleep(2)
#发送
dr.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
sleep(3)



#智能等待

# dr = webdriver.Firefox()
# dr.get("https://www.jd.com")
# sleep(3)     #强制等待
# unti=ui.WebDriverWait(dr,10)   #设置一个智能等待
# #定位要出现的元素
# unti.until(lambda dr:dr.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[4]/ul[1]/li[2]/a').is_displayed())
#模拟鼠标操作
"""
dr = webdriver.Firefox()
dr.get("https://qzone.qq.com")
sleep(3)
#鼠标移动
ww=dr.find_elements_by_class_name('cate_menu_item')
for i in ww:
    #动作链：动作链控制鼠标移动到某个元素的中心点
    ActionChains(dr).move_to_element(i).perform()
    sleep(2)
#鼠标拖拽
dr.switch_to_frame('login_frame')
sleep(3)
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="u"]').send_keys('1789898380')
sleep(3)
dr.find_element_by_xpath('//*[@id="p"]').send_keys('qhjfq99')
sleep(3)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(3)
ee=dr.find_element_by_id('tcaptcha_iframe')
dr.switch_to.frame(ee)
sleep(3)
ww=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
ActionChains(dr).drag_and_drop_by_offset(ww,160,0).perform()
"""
# 登录QQ邮箱
# 打开网页的代码添加一句

# dr = webdriver.Firefox()
# # 访问网址
# dr.get("https://www.baidu.com")
# sleep(2)
# dr.get('https://mail.qq.com/cgi-bin/loginpage')
# sleep(3)
# dr.switch_to.frame('login_frame')
# sleep(2)
# #选择账号密码登录
# dr.find_element_by_id('switcher_plogin').click()
# sleep(5)
# #输入QQ号
# dr.find_element_by_id("u").send_keys("1719652243")
# sleep(8)
# #输入QQ密码
# dr.find_element_by_name("p").send_keys("D.1996949")
# sleep(8)
# #单击登录
# dr.find_element_by_id("login_button").click()
