#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Date:2021-03-24
# @autor Lrving


# 展示信息

def showMenu():
    menu_info = """
                   Htek 自动化管理系统
    ┍———————————————————————————————————————————-—┑
    │         ========主菜单========               | 
    │         1 话机信息                           
    │         2 测试用例                              
    │         3 查看日志                              
    │         4 退出当前系统                           
    │         =====================                   
    │        说明：通过数字或者↑↓方向键选择菜单           
    ┕————————————————————————————————————————————┙
    """
    print(menu_info)


showMenu()


def phone_information():
    phone_info = """
    ┍———————————————————————————————————————————-—┑
    │         ========主菜单========               | 
    │         1 话机信息                           
    │         2 测试用例                              
    │         3 查看日志                              
    │         4 退出当前系统                           
    │         =====================                   
    │        说明：通过数字或者↑↓方向键选择菜单           
    ┕————————————————————————————————————————————┙
    """
    print(phone_info)


def testRail():
    testRail_info = """
    ┍————————————————————┑
    | ======测试用例===== 
    | 1 录入测试用例
    | 2 查询测试用例
    |
    |
    ┕————————————————————┙
    """
    print(testRail_info)


print("请选择：", end="")
number = int(input())
if number == 1:
    phone_information()
elif number == 2:
    testRail()
elif number == 0:
    print("已经返回到主界面")
    showMenu()
