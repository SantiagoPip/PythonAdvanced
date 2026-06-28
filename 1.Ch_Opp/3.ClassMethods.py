class MyClass:
    my_var = 100
    def __init__(self,value): #Dunder method
        self.value = value
    #Dunder method for string
    def __str__(self):
        return "this is a string"
    @classmethod
    def _change_value(cls, new_value):
        MyClass.my_var = new_value
    @staticmethod
    def dummy():
        print("This is a dummy method")


obj1 = MyClass(10)
print(f"{obj1.my_var} valor original")
obj2 = MyClass(10)
print(obj2.my_var)
obj1._change_value(10000000)
print(MyClass.my_var)
print(obj2.my_var)
obj3 = MyClass(1)
print(obj3.dummy())