#！/user/bin/python
#-*-coding:utf-8-*-
import logging
import datetime

#日志目录（日志文件夹）
LOG_DIR = "E:\\QQ\\log1\\"
#日期.txt
#创建一个日志文件名
a=LOG_DIR + str(datetime.datetime.now().date()) + '.txt'
print(a)

#logging----->python定义日志的库
#定义日志输出的格式
formatter=logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')
print(formatter)

#logging的两种输出方式
#第一种：输出到pycharm的控制台
c=logging.StreamHandler()
#第二步：添加日志的样式
c.setFormatter(formatter)
#第二种：输出到文本
w=logging.FileHandler(a,encoding="utf-8")
#添加日志样式
w.setFormatter(formatter)

def get_logger(filename):
    l=logging.getLogger(filename)    #获取执行日志的脚本名字
    l.addHandler(c)                #添加输出内容到控制台
    l.addHandler(w)                 #添加输出内容到文本
    l.setLevel(logging.INFO)         #定义日志的等级   INFO--->最低等级
    return l

# log=get_logger()
# log.info("jifjejojeniurejjeijivjjij")
# log.error("wiuvjoemjooejo")




