#coding=utf-8

class Case1():


    def case(self,**kwargs):
        if "b" in kwargs.keys():
            b = kwargs["b"]
        if "a" in kwargs.keys():
            a = kwargs["a"]
        if "c" in kwargs.keys():
            c = kwargs["c"]
        if "d" in kwargs.keys():
            d = kwargs["d"]
        print(a+b)
Case1().case(a='c',b='s')