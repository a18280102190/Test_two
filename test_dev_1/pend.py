# def true():return  True
# lambda  : True
# def add(x,y):
#     return x+y
#
# add(3,5)

# lambda x,y:x+y

# lambda  x:x<=(a,b)
# def func1(x):
#     return x<=(a,b)
#
#
# lambda  item:item[1]
# def func2(item):
#     return item(1)

# a=[1,2,3,4,5,6,7]
# list(filter(lambda x:x>2 , a))
# a=[1,2,3]
# list(map(lambda x:x+1,a))
# b=[4,5,6]
# list(map(lambda x:x+1,b))
# a=[1,2,3]
# b=[4,5,6]
# list(map(lambda x,y:x+y,a,b))
# from functools import reduce
# help(reduce)

# from functools import reduce
# reduce(lambda x,y:x+y ,[2,3,4],1)
# for i in zip((1,2,3),(4,5,6)):
#     print(i)

# dicta ={'a':'aa','b':'bb'}
# dictb = zip(dicta.values(),dicta.keys())
# print(dict(dictb))

# def func():
#     a = 1
#     b = 2
#     return a+b
#
# def sum(a):
#     def add(b):
#         return  a+b
#     return add
# #add 函数名称或函数的引用
# #add()函数的调用
# num1 = func()
# num2 = sum(2)
# print(num2(4))
# print(type(num1))
# print(type(num2))

# 闭包计数器
# def counter(FIRST=0):
#     cnt = [FIRST]
#     def add_one():
#         cnt[0] +=1
#         return cnt[0]
#
#     return  add_one
# num5 = counter(5)
# num10 = counter(10)
#
# print(num5())
# print(num10())

# a * x + b = y
# def a_line(a,b):
#     def arg_y(x):
#         return a*x+b
#     return  arg_y
# #a=3 b=5
# #x=10 y=?
# #x=20 y=?
# line1 = a_line(3,5)
# line2 = a_line(5,10)
# print(line1(10))
# print(line2(20))

# import time
# def timmer(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         stop_time= time.time()
#         print('运行时间多少 %s' % (stop_time-start_time))
#     return  wrapper
#
#
# @timmer
# def i_can_sleep():
#     time.sleep(3)
#
# # start_time = time.time()
# i_can_sleep()
# stop_time = time.time()
# print('运行时间多少 %s' % (stop_time-start_time))

# 闭包计时器固定值操作
# def counter():#定义外部函数
#     cnt = [0]
#     def add_one():#定义内部函数
#         cnt [0] +=1#函数每运行一次，进行+1操作
#         return cnt[0]
#     return add_one #add 函数名称或函数的引用
#
# num1 = counter()# add()函数的调用
# print(num1())

# #闭包计时器传值操作
# def counter(FIRST = 0):#进行传值操作 #定义外部函数
#     cnt = [FIRST]#进行传值操作
#     def add_one():#定义内部函数
#         cnt [0] +=1#函数每运行一次，进行+1操作
#         return cnt[0]
#     return add_one #add 函数名称或函数的引用
#
# num5 = counter(5)# add()函数的调用
# num10 = counter(10)# add()函数的调用
#
# print(num5())
# print(num5())
# print(num10())
# print(num10())

# a*b+x=y,计算题
# def a_line(a,b):
#     def arg_y(x):
#         return a*x+b
#     return arg_y
# 优化之后的代码：
# def a_line(a,b):
#     return lambda x:a*x+b
#
#     return arg_y
#
# line1 = a_line(3,5)#a,b的赋值
# line2 = a_line(5,10)
# print(line1(10))#x的赋值
# print(line2(8))
# 闭包是直接传递函数，函数是直接传递变量


# import time
#
# def i_can_sleep():#函数名称
#     time.sleep(3)
#
# start_time = time.time()#定义两个变量，开始时间
#
# i_can_sleep()#i_can_sleep函数执行时间被start_time and stop_time统计
#
# stop_time = time.time()#定义两个变量，结束时间
#
# print('函数执行需要 % s秒' % (stop_time-start_time))#使用结束的时间减去开始的时间，等到函数执行的时间
# 装饰器的定义
# import time
#
# def timmer(func):#(3)接受一个func变量
#     def wrapper():#(4)讲传递给内部的函数，内部函数中定义了start_time and stop_time ,func函数将会被这两个统计时间
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print('函数执行需要 % s秒' % (stop_time-start_time))#(5)使用结束的时间减去开始的时间，等到函数执行的时间
#     return wrapper#(6)返回wrapper
#
# @timmer#(2)当调用i_can_sleep时，会被发现，将被传递到封装的函数中
# def i_can_sleep():#函数名称
#     time.sleep(3)
# i_can_sleep()#(1)当调用该函数时，发现timmer语法糖

# 装饰器带参数的使用
# def tips(func):
#     def nei(a,b):
#         print('start')
#         func(a,b)
#         print('stop')
#     return nei
#
# @tips#装饰糖必须是有意义的
# def add(a,b):
#     print(a+b)
#
# print(add(3,5))

# def new_tips(argv):
#     def tips(func):
#         def nei(a,b):
#             print('start % s %s' % (argv,func.__name__))#取函数的名字
#             func(a,b)
#             print('stop')
#         return nei
#     return tips
#
# @new_tips('add_1')#装饰糖必须是有意义的
# def add(a,b):
#     print(a+b)
#
# @new_tips('sub_1')# 装饰糖必须是有意义的
# def sub(a, b):
#     print(a - b)
#
# print(add(3,5))
# print(sub(10,5))

# from mymod import new_top#两种方法相同
# import mymod
# #导入mymod模块
# mymod.new_top
# #调用mymod模块，调用new_top函数

# 面向过程编程，更适合机器运行的，这将是一步一步的去运行
# user1 = {'name':'tom','hp':100}
# usre2 = {'name': 'jerry', 'hp': 80}
#
# def print_role(rolename):
#     print('name is %s ,hp is %s' % (rolename['name'],rolename['hp']))
#
# print_role(user1)


# 面向对象编程，更适合人的思维，将相同的事物进行归类
# class Top():#定义一个类，类一大写开头
#     def __init__(self,name,hp):#预订了一些数据
#         self.name = name # 变量被称作属性
#         self.hp = hp
#     def print_role(self):#定义一个方法
#         print('%s %s' % (self.name,self.hp))
#
# user1 = Top('tom',100)#引用类，叫做类的实例化
# user2 = Top('jerry',80)
# user1.print_role()
# user2.print_role()

# class Top():
#     def __init__(self,name ,hp , occu):  #(修改或者新添,请添加方法和属性来修改)
#         self.name = name#(__name时，是不被实例访问的)
#         self.hp = hp
#         self.occu = occu
#
#     def print_Top(self):
#         print('玩家名称：% s , 生命值 %s ，玩家职业 %s' % (self.name,self.hp,self.occu))
#
#     def Add_name(self,newname):#新添加一个方法(类的封装)
#         self.__name = newname#增加一个属性
#
#
# class Monser():
#     '定义怪物类型'
#     pass
#
# uesr1 = Top('tom',100,'战士')
# uesr2 = Top('jerry',80,'法师')
#
# uesr1.print_Top()
# uesr2.print_Top()
#
# uesr1.Add_name('jk')#在uesr1中添加一个新的玩家名
# uesr1.print_Top()#进行输入出
#
# uesr1.name = ('tk')
# uesr1.print_Top()

# try:
#     class Top():
#         def __init__(self,name,hp,coou):
#             self.name = name
#             self.hp = hp
#             self.coou = coou
#
#         def wanjia(self):
#             print('玩家名称： % s 玩家生命值：%s  玩家职业 %s' %(self.name,self.hp,self.coou))
#
#         def add_one(self,newname):
#             self.name = newname
#
#         def add_two(self,newname1):
#             self.name = newname1
#
#     class guaiwu():#父类
#         def __init__(self,hp):
#             self.hp=hp
#
#         def run(self):
#             print('移动到某个位置')
#
#
#     class xiaoguai(guaiwu):#类的继承
#         '小型怪'
#         def __init__(self,hp):
#             super().__init__(hp)
#         def ok(self):
#             print('小型怪')
#
#     class Boss(guaiwu):
#         'boss类型的怪物'
#         def __init__(self,hp):
#             super().__init__(hp)
#         def OK(self):
#             print('我是终极boss')
#
#     a1 = guaiwu(100)
#     print(a1.hp)
#     print(a1.run())
#     a2 = xiaoguai(10)
#     print(a2.hp)
#     print(a2.ok())
#
#     a3 = Boss(800)
#     print(a3.hp)
#     print(a3.OK())
#     print(type(a1))
#
#     print(isinstance(a2,guaiwu))#检查类的关系
#
#     # uesr1 = Top('tom',100,'战士')
#     # uesr1.wanjia()
#     #
#     # uesr1.add_one('jk')
#     # uesr1.wanjia()
#     #
#     # uesr1.add_two('tk')
#     # uesr1.wanjia()
#
# except Exception as  e:
#     print('请注意新添calls： %s' % (e))

# with自定义语句
# 类和异常的结合
# class Testwith():
#     def __enter__(self):
#         print('run')
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_tb is None:
#             print('正常结束')
#         else:
#             print('has error %s' % (exc_tb))
#
# with Testwith():
#     print('Test is runing')
#     raise Exception('test')

# import threading#仿真java线程模型子集的线程模块
# import time
# from threading import current_thread#当前线程运动的情况进行显示，#当前线程运行的一个显示
#
# def add_one(ag1,ag2):
#     print(current_thread().getName(),'start')
#     print('%s %s '% (ag1,ag2))
#     time.sleep(2)
#     print(current_thread().getName(),'stop')
#
# for i in range(1,6,1):#我们循环了五次
#     t1 = add_one(i,i+1)
#     t1 = threading.Thread(target=add_one,args=(i,i+1))#target传递参数名，args传递参数
#     t1.start()
#
# print(current_thread().getName(),'end')

# import threading
# from threading import current_thread
# #
# #
# class my(threading.Thread):
#     def run(self):
#         print(current_thread().getName(), 'start')
#         print('run')
#         print(current_thread().getName(), 'stop')
#
#
# t1 = my()
# t1.start()
# t1.join()
#
# print(current_thread().getName(), 'end')


# class Top():
#     def __init__(self,name,hp,coou):
#         self.name = name
#         self.hp = hp
#         self.coou = coou
#
#     def topone(self):
#         print('玩家名称 %s 生命值 %s 职业 %s' % (self.name,self.hp,self.coou))
#
#
#     def toptow(self,newname,newhp,newcoou):
#         self.name = newname
#         self.hp = newhp
#         self.coou = newcoou
#
#
# class Buuton(Top):
#     def __init__(self,name,hp,coou):
#         super().__init__(name,hp,coou)
#
#
# a1 = Top('kaer',1500,'战士')
# a1.topone()
#
# a1.toptow('MTN',2000,'法师')
# a1.topone()
#
# a2 = Buuton('TNT',800,'射手')
# a2.topone()
#
# print(isinstance(a2,Top))

#队列
# from threading import Thread,current_thread#可以实现多线程，如：多个生产，多个消费
# import time
# import random#随机，随机产生数据
# from queue import Queue #队列
#
# queue = Queue(5)#队列长度是5，最多只能容纳五个数字
#
# class a(Thread):
#     def run(self):#定义一个run函数
#         name = current_thread().getName()#提取当前线程的名字，便于区分生产者和消费者
#         nums = range(100)#生产者的选择范围
#         global queue#global全球变量
#         while True:#死循环
#             num = random.choice(nums)#随机选择一个数字
#             queue.put(num)#通过Q.put放入指定的队列当中
#             print('生产者 %s 生产力数据 %s' % (name,num))
#             t = random.randint(1,3)#放入之后就让生产者进行休眠，#随机的休眠时间，向队列里面添加数字
#             time.sleep(t)
#             print('生产者 %s 睡眠了 %s' % (name, t))
#
# class b(Thread):
#     def run(self):#消费者的run的方法
#         name = current_thread().getName()#提取当前线程的名字，便于区分生产者和消费者
#         global queue#global全球变量
#         while True:
#             num = queue.get()#消费者的向队列中提取数字，#提取数字
#             queue.task_done()#该方法，封装了线程同步和等待的代码
#             print('消费者 %s 消费了数据 %s' % (name,num))#消耗了具体的数字
#             t = random.randint(1,5)#随机的休眠时间，进行输出
#             time.sleep(t)
#             print('消费者 %s 睡眠了 %s' % (name, t))
#
# p1 = a(name= 'p1')
# p1.start()
#
# c1 = b(name= 'c1')
# c1.start()
#
# c2 = b(name= 'c2')
# c2.start()


# import re#正则表达式#标准库

#正则表达式常用的字符：
#.(点：功能：任意匹配单个字符)
# p = re.compile('.')
# print(p.match('d'))
# ^(该功能：以什么内容做开头,主要用于搜索和替换,表示从开头进行搜索)
#$ 以什么内容做结尾，从后面向前面做匹配
#* 匹配前面的字符0或者多次，贪婪模式
#+ 前面的字符出现1次或者多次
#？ 表示字符出现0次或者1次
#{m} 大括号 这个里面必须填写一些内容，表示前面的字符出现指定的次数
#{m,n} 表示 字符出现(如：{4,6}4到6次)
#[] 中括号 任意一个字符匹配成功，就是成功，如：c[dcb]t.会匹配 cct,cdt,abt
# | 表示选择字符选择左右两边任意一边，通常会和括号结合使用
###以上属于单个字符
#\d转移字符，表示匹配的内容是一串数字，匹配[0-9]这样的数字
#\D 和 \d功能是相反的，匹配不包含数字的
#\s表示匹配的是一个字符串
#()小括号：进行分组

#^$特殊符号组合在一起，表示这一行是空行，文本中存在的空行是就可以使用这个组合
#.*? 不使用贪婪模式，只使用匹配第一个，我们匹配上的内容 #编写网页时，会使用到




# import re
# p = re.compile('.{3}')#任意字符出现三次将会被匹配
# print(p.match('dat'))
# p = re.compile(r'(\d+)-(\d+)-(\d+)')#r功能是不会进行转译,使用\d进行数字匹配，使用()小括号进行分组，使用+号匹配多个数字
# print(p.match('2018-05-06').group(1))#使用group取出某一部分，在group的括号中写入1的话，只取出第一个括号的部分
# print(p.match('2018-05-06').groups())#使用groups取出全部
#
# #可直接赋给变量使用,match匹配功能，match是需要和正则一一对应的，完全匹配，必须提前清楚，macth只会匹配第一个字符
# a,b,c = p.match('2018-05-06').groups()
# print(a,b,c)

# #search 是搜索功能，元字符和输入内容完全匹配，search，如果对第一个字符匹配失败，会继续匹配下一个字符，以此内推
# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.search('xx2018-05-06xx'))

#字符替换操作
#sub('','','')可替换函数
# one = '182-1111-2222 # 发发发发'
# p2 = re.sub(r'#.*$','',one)#第一个''是选择需要替换的字符内容，第二个''是更新的内容，记得添加函数
# print(p2)
# p3 = re.sub(r'\D',' ',p2)#只保留数字
# print(p3)
# re.findall()可以进行多次匹配


#time datatime 日期和时间函数库
# import time
# print(time.time())#1976到现在的秒数
# print(time.localtime())#可以获取当期的时间
# print(time.strftime('%Y-%m-%d  %H:%M:%S' ))#适用于人类阅读
# import time
# import datetime
# print(datetime.datetime.now())#获取当期年月日
# newtime = datetime.timedelta(minutes=10)#进行时间的计算，并让时间偏移10分钟
# print(datetime.datetime.now() + newtime)#对当前时间进行增加
#
# one_day = datetime.datetime(2060,8,28)#直接赋值
# new_day = datetime.timedelta(days=10)#将天数偏移增加10天
# print(one_day + new_day)#输出已有的天数加偏移增加的天数


#数学相关库
#math 可用于计算正弦值 和 余弦值
#random 随机

# import random
#
# print(random.randint(1,65))#随机选择一个数字
# print(random.choice(['aa','cc','bb']))#随机选择一个字符

# import os
# print(os.path.abspath('..'))#获取上一层路径
# print(os.path.abspath('.'))#相对路径根据你的点获取绝对路径
# print( os.path.exists('/Users'))#判断路径是否存在
# print( os.path.isfile('/Users'))#判断文件是否存在
# print( os.path.isdir('/Users'))#判断是否是目录
# os.path.join('/t/a/','/c/s')#路径拼接,拼接比喻


# name  = 'Tom'
# hp = 100
# print('I is {0},I hp {1},{0}'.format(name,hp))
#
# list1 = [0,1,2,3]
# dict1 = {'name':'jerry','hp':100}
#
# print('I is {}, I is {}'.format(list1,dict1))
# dict1 = {'name':'jerry','hp':100}
# print('we name : {name}, i in name : {hp}'.format(**dict1))
# namelist  = ['lili','tom','jerry']
#
# print('we name : {}`{} and {}'.format(*namelist))

# list1 = [0,1,2,3]
# dict1 = {'name':'jerry','hp':100}
#
# name = 'Tom'
# age = 123
# print(f"wa name : {name},one : {age},two :{list1[1]},three{dict1['hp']}")
# print(f"we name : {name.upper()}")
# print(f"i is {(lambda x:x+1)(2)}")
# print(f" wa name {11}")

# a = open('name.txt',encoding='utf-8')
# print(a.read())
# a.close()
# with open('name.txt',encoding='utf-8') as a:
#     while True:
#         txt = a.readline()
#         if txt:
#             print(txt)
#         else:
#             break
# try:
#     with open('name.tx',encoding='utf-8') as a:
#         while True:
#             txt = a.readline()
#             if txt:
#                 print(txt)
#             else:
#                 break
# except Exception as e:
#     print('请输入正确的文件名: %s' % (e))
# # else:
# #     print('这是正确的')
# finally:
#     print('无论对与错都执行')

# from threading import current_thread,Thread
# from queue import Queue
# import time
# import random
# queue = Queue(5)
# class Top(Thread):
#     def run(self):
#         name = current_thread().getName()
#         nums = range(100)
#         global queue
#         while True:
#             num = random.choice(nums)
#             queue.put(num)
#             print('生产者%s 生产力%s' % (num,name))
#             t = random.randint(1,3)
#             time.sleep(t)
#             print('生产者%s 睡眠了%s' % (name,t))
# class Button(Thread):
#     def run(self):
#         name = current_thread().getName()
#         global queue
#         while True:
#             num = queue.get()
#             queue.task_done()
#             print('消费者%s 消费力%s' % (name,num))
#             t = random.randint(1,5)
#             time.sleep(t)
#             print('消费者%s 睡眠了%s' % (name, t))
#
# p1 = Top(name='p1')
# p1.start()
#
# c1 = Button(name='c1')
# c1.start()

# x = 20
# if x>5:
#     raise Exception("这是一个异常")
# import random
# me_hp = 2000
# me_lke  = random.randint(10,20)
# you_hp = 2000
# you_lke = random.randint(10,20)
# while True:
#     me_hp = me_hp - you_lke
#     print(f"我方hp:{me_hp}")
#     you_hp = you_hp - me_lke
#     print(f"敌人hp:{you_hp}")
#     if me_hp < 0:
#         print('游戏结束')
#         break
#     elif you_hp < 0:
#         print('敌人输了')
#         break
# def func1(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# func1(b=2,a=1,c=3,d=4)
# list1 = []
# for i in range(1,4):
#     list1.append(i**2)
# print(list1)

# import json
# data = {
#     'name':['tom','jerry'],
#     'hp':100,
#     'coou':'mt'
# }
# print(type(data))
# data1 = json.dumps(data)
# print(data1)
# print(type(data1))
# data2 = json.loads(data1)
# print(data2)
# print(type(data2))

# class Top():
#     def __init__(self,name,hp,coou):
#         self.name = name
#         self.hp = hp
#         self.coou = coou
#
#     def top(self):
#         print(f"姓名：{self.name},血量：{self.hp},职业：{self.coou}")
#
#     def addtop(self,newname):
#         self.name = newname
#
# class Button(Top):
#     def __init__(self,name,hp,coou):
#         super().__init__(name,hp,coou)

# user1 = Top('tom',100,'mm')
# user1.top()
#
# user1.addtop('MT')
# user1.top()
#
# user2 = Button('jerry',200,'dog')
# user2.top()
# import os
# # os.rmdir('test1')
# # os.mkdir('test1')
# print(os.listdir("./"))

import time

print(time.asctime())
print(time.time())
print(time.strftime('%Y-%m-%d-%H:%M:%S'))







