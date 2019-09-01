#！/user/bin/python
#-*-coding:utf-8-*-
import allure
import pytest

#feature：标注测试用例是属于哪一个模块的
@allure.feature("模块一")
def test_1():
    assert 0==0
@allure.feature("模块一")
def test_2():
    assert 2<3

#story：对一个测试用例进行详细描述
@allure.feature("模块二")
@allure.story("这是一个很厉害的测试用例")
def test_3():
    assert 0>1

@allure.feature("模块二")
@allure.story("这是一个很垃圾的测试用例")
def test_4():
    """
    对函数的参数的返回值的注释
    自我感觉良好
    """
    #测试用例的描述是通过函数的注释来获取到的
    assert "小可爱真好看"

#测试用例的优先级
"""
Blocker级别：阻塞中断缺陷
Critical级别：严重缺陷
Normal级别：普通缺陷
Minor级别：次要
Trivial级别：轻微
"""
@allure.feature("模块三")
@allure.severity("blocker")
def test_5():
    assert 0 ==0
@allure.feature("模块三")
@allure.severity("critical")
def test_6():
    assert 0 >1
@allure.feature("模块三")
@allure.severity("normal")
def test_7():
    assert 0 <1
@allure.feature("模块三")
@allure.severity("minor")
def test_8():
    assert 0 ==1
@allure.feature("模块三")
@allure.severity("trivial")
def test_9():
    assert 0!=1
#git---svn---jenkins---执行python代码---报告----访问某个网址
#step  记录测试用例中的一些步骤，日志代码可以通过step记录到报告中
#isinstance(参数一，参数二)判断数据类型，参数一和参数二是否是同一个类型；是---true;不是---false
@allure.step("字符串相加：{0},{1}")
def str_add(str1,str2):
    if not isinstance(str1,str):
        return f"{str1}不是字符串类型的"
    if not isinstance(str2,str):
        return f"{str2}不是字符串类型的"
    return str1 + str2
@allure.feature("模块四")
def test_10():
    str1="hello"
    str2="world"
    assert str_add(str1,str2)=="helloworld"

#issue和testcase
#对issue和testcase生成一个网址
@allure.step("字符串相加：{0}，{1}")
#测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    print('hello')
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2

@allure.feature("模块五")
@allure.story('test_story_01')
@allure.severity('blocker')
@allure.issue("http://www.baidu.com")   #存放bug出现的问题
@allure.testcase("http://www.testlink.com") #存放的测试用例的信息
def test_case():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'

#attach


