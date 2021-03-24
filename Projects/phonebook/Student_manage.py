#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def display_function():
    print("1.新增名片\n2.显示全部\n3.名片\n0.退出系统")


def add_list():
    user_name = input("请您输入姓名：")
    user_phone = input("请您输入电话：")
    user_qq = input("请您输入qq号：")
    user_email = input("请您输入邮箱：")
    dic = {}
    dic['姓名'] = user_name
    dic['电话'] = user_phone
    dic['qq'] = user_qq
    dic['邮箱'] = user_email
    user_card.append(dic)
    print("新增名片成功！")


def print_all_card():
    print("姓名\t\t\t\t电话\t\t\t\tqq\t\t\t\t邮箱\t\t\t\t")
    for i in range(0, len(user_card)):
        # print_kwargs(**user_card[i])
        print("{:<16}{:<16}{:<16}{:<16}".format(user_card[i]['姓名'], user_card[i]['电话'], user_card[i]['qq'],
                                                user_card[i]['邮箱']))


def find_card():
    find_user_name = input("请输入您要查找的用户的姓名：")
    find_num = 0
    can_not_find = 0
    for i in user_card:
        if i['姓名'] == find_user_name:
            find_num = user_card.index(i)
            print("找到了，信息如下")
            print(i)
            can_not_find = 1
            break
    if can_not_find == 0:
        print("您查找的用户不存在！")
        return find_card()
    inp_find = int(input("【1】修改\n【2】删除\n【3】返回上一级菜单"))
    if inp_find == 1:
        user_change_key = input("请输入需要修改的类别：")
        user_change_value = input("请输入您需要修改的内容：")
        user_card[find_num][user_change_key] = user_change_value
        print("修改完成！")
        print(user_card[find_num])
    elif inp_find == 2:
        del user_card[find_num]
        print("删除完成！")
        print_all_card()
    elif inp_find == 3:
        return display_function()


def main_code():
    while 1:
        display_function()
        user_doing = int(input("请输入您希望执行的操作："))
        if user_doing == 1:
            add_list()
        elif user_doing == 2:
            print_all_card()
        elif user_doing == 3:
            find_card()
        elif user_doing == 0:
            print("退出系统！")
            break
    return


user_card = []
main_code()


