# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 07:40:38 2026

@author: SantiagoAlejandroMor
"""
class MyClass:
    # Constructor
    def __init__ (self,var1,var2,var3):
        self.var1 = var1 # Public 
        self.__var2 = var2  #Private
        self._var3 = var3 #Protected
    # Class Methods
    def func1(self):
        print(f"Hello {self.var1} {self.__var2}")
    def func2(self):
        print(f"Hello Globe {self.var1} {self.__var2}")
# Create Python Object 
#obj = MyClass("Vanessa","Montoya","Arias")
#obj2 = MyClass("Santiago","Moreno","Espitia")
#obj2.var1 = "Vanessa"
#obj.func1()
#obj2.func2()
obj = MyClass("abc","def","xyz")

obj.var1 = "pqr"
print(obj.var1)
obj.func1()

obj.var2 = "stu"
obj.func2()
obj._MyClass__var2 = "dd"
print(obj.var2)
obj.func2()
print(obj._MyClass__var2)
obj.func2()

