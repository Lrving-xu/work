#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @autor Lrving


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, school, name, age):
        self.school = school
        super().__init__(name, age)

    def get_school(self):
        return self.school

    def green(self, n):
        print("{0}'s green is {1} ".format(self.name, n))


stu1 = Student("青山", "XU", 18)
stu1.green('三年级')
print(stu1.get_name())
print(stu1.get_age())
print(stu1.get_school())
