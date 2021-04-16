# -*- coding: utf-8 -*-
import sys
sys.path.append('./TestModule_Python')
import MyClass

c = MyClass.MyClass()

c.printHello()

c.setName('Hoge')
c.printHello()
