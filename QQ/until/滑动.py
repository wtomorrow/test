#！/user/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
#获取手机屏幕的大小
def hh_left(dr,t=500):
    l = dr.get_window_size()
#放缩屏幕
    x1 = l['width']*0.7
    x2 = l['width']*0.9
    y1 = l['height']*0.3
    dr.hh(x2,y1,x1,y1,t)
# y2 = l['height']*0.5
#向左滑动
def hh_right(dr,t=300):
    l = dr.get_window_size()
    x1 = l['width'] * 0.5
    x2 = l['width'] * 0.8
    y1 = l['height'] * 0.3
    dr.swipe(x1,y1,x2,y1,t)
def hh_up(dr,t=500):
    l = dr.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.3
    y2 = l['height'] * 0.5
    dr.swipe(x1, y2, x1, y1,t)
def hh_down(dr,t=400):
    l = dr.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.3
    y2 = l['height'] * 0.5
    dr.swipe(x1, y1, x1, y2,t)








