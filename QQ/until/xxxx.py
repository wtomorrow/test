#！/user/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
from time import sleep
import yaml,pytest
with open (file=r"E:\QQ\data\login.txt",mode='r',encoding="utf-8") as f:
    t=f.read().split(';')
s=[]
for i in t:
    k=i.replace('\n','').split(',')
    s.append(tuple(k))
print(s)
