#！/user/bin/python
#-*-coding:utf-8-*-
from appium import webdriver

#向上滑动
def hh_up(foo,t=500):
    l = foo.get_window_size()
    x1 = l['width'] * 0.5
    x2 = l['width'] * 0.5
    y1 = l['height'] * 0.1
    y2 = l['height'] * 0.9
    foo.swipe(x1, y2, x1, y1,t)
#向下滑动
def hh_down(foo,t=400):
    l = foo.get_window_size()
    x1 = l['width'] * 0.5
    x2 = l['width'] * 0.5
    y1 = l['height'] * 0.3
    y2 = l['height'] * 0.5
    foo.swipe(x1, y1, x1, y2,t)

