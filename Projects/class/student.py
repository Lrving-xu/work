#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @autor Lrving

# class Student(object):
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

#     def get_grade(self):
#         return self.grade



# stu_1 = Student('Lrving',18,3)
# print("""
# 学生的信息：
# 姓名: %s
# 年龄: %d
# 年级: %d
# """ %(stu_1.get_name(),stu_1.get_age(),stu_1.get_grade()))




"""
1.编写一个程序，判断学生作业是否完成，如果完成，老师会给予表扬，否则会给予批评。
2.定义一个学生类——具有写作业，班级熟悉
3.定义一个老师类——具有批改作业，表扬批评

"""

class Student:
    def __init__(self,name,grade,subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def do_work(self,time):
        if self.grade > 3 and time > 2:
            return True
        elif self.grade <3 and time > 0.5:
            return True
        else:
            return False

class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject

    def evaluation(self,result = True):
        if result:
            return "You are great"
        else:
            return "You should study hard"

stu_Lrving = Student('Lrving',5,'math')
tea_wang = Teacher('wang','math')
teacher_said = tea_wang.evaluation(stu_Lrving.do_work(1))
print("Teacher {0} said : {1} {2}".format(tea_wang.name,stu_Lrving.name,teacher_said))

stu_xu = Student('xu',6,'english')
tae_zhang = Teacher('xuan','english')
teacher_note = tae_zhang.evaluation(stu_xu.do_work(4))
print("Teacher {0} said : {1} {2}".format(tae_zhang.name,stu_xu.name,teacher_note))