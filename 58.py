import shutil
import os
import zipfile


# class Example:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
# e = Example(8, 6)
# print(e.add())
#
# class Parent:
#     def __init__(self, a):
#         self.a = a
#     def method1(self):
#         print(self.a*2)
#     def method2(self):
#         print(self.a+'!!!')
#
# class Child(Parent):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def method1(self):
#         print(self.a*7)
#     def method3(self):
#         print(self.a + self.b)
#
# p = Parent('hi')
# c = Child('hi', 'bye')
#
# print('Parent method 1: ', p.method1())
# print('Parent method 2: ', p.method2())
# print()
# print('Child method 1: ', c.method1())
# print('Child method 2: ', c.method2())
# print('Child method 3: ', c.method3())
#
#
# class Shark():
#     def swim(self):
#         print("The shark is swimming.")
#
#     def swim_backwards(self):
#         print("The shark cannot swim backwards, but can sink backwards.")
#
#     def skeleton(self):
#         print("The shark's skeleton is made of cartilage.")
#
#
# class Clownfish():
#     def swim(self):
#         print("The clownfish is swimming.")
#
#     def swim_backwards(self):
#         print("The clownfish can swim backwards.")
#
#     def skeleton(self):
#         print("The clownfish's skeleton is made of bone.")

# sammy = Shark()
# sammy.skeleton()
#
# casey = Clownfish()
# casey.skeleton()


# # from tkinter import *
# # root = Tk()
# # mainloop()
#
# hello_label = Label(text='hello', font=('Verdana', 24, 'bold'), bg='blue', fg='white')
# hello_label = Label(text='hello')
# hello_label.grid(row=0, column=0)


# entry = Entry()
# entry.grid(row=0, column=0)



# num = 0
# while (num < 10):
# 	print(num)
# 	num = num + 1	#update the value of num by 1

# def helloWorld():
#     print("Hello World")
# helloWorld()


# def addNumbers(num1, num2):
# 	sum = num1 + num2
# 	print(sum)
# 	return
# addNumbers(2,3)
# addNumbers(4,5)


# import math
# math.pow(5,4)
#
# import math
# a = math.floor(4.3)
# b = math.floor(10.9)
# print (a)
# print (b)
#
# import math
# a = math.ceil(4.3)
# b = math.ceil(10.9)
# print (a)
# print (b)

# a = abs(10)
# b = abs(-10)
# print (a)
# print (b)
#
# import math
# a = math.log(10)
# b = math.log(10,2)
# print (a)
# print (b)
#
# import math
# a = math.sqrt(9)
# b = math.sqrt(16)
# print (a)
# print (b)
#
# str = " "
# iter = ("I","am","awesome.")
# a = str.join(iter)
# print(a)

# import threading;
# import time;


# class Thread1(threading.Thread):
#     def run(self):
#         for i in range(0, 10):
#             time.sleep(2);
#             print
#             "Thread1: ", i;
#
#
# class Thread2(threading.Thread):
#     def run(self):
#         for i in range(0, 10):
#             time.sleep(4);
#             print
#             "Thread2: ", i;
#
#
# t1 = Thread1();
# t2 = Thread2();
# t1.start();
# t2.start();

# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(3) == 5
# x = [2, 4]
# x += [6, 8]
# print(x[2]//x[0])

# x = [2, 4]
# x = x * 3
# print(x[3])

# x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
# sum = 0
# for i in x:
#     sum += i
# print(sum)

# res = 0
#
# for x in nums:
#     if (x % 2 == 0):
#         continue
#     else:
#         res += x
#
# print(res)

# numbers = range(10)
#
# list = [1, 1, 2, 3, 5, 8, 13]
# print(list[list[4]])

#suma a n numere naturale
# N = int(input())
#your code goes here
#
# i = 1
# sum = 0
# while (i <= N):
#     sum = sum + i
#     i = i + 1
# print(sum)

# def area(x, y):
#    #your code goes here
#    return x*y
#
# w = int(input())
# h = int(input())
#
# #call the function
# print(area(w, h))

# def print_numbers():
#   print(1)
#   print(2)
#   return
#   print(4)
#   print(6)

# def sum(x):
#       res = 0
#       for i in range(x):
#           res += i
#       return res
#
# # print(sum(4))
#
# def print_nums(x):
#   for i in range(x):
#     print(i)
#     return
# print_nums(10)
#
# def search(text, word):
#   if(text.find(word)):
#     print("Word found")
#   else:
#     print("Word not found")
