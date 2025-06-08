class A:
    def __init__(self):
        print("__init__ of class A")
    def method1(self):
        print("Always study")
    def method(self):
        print("you will get all of my property and method")
class B(A):
    def __init__(self):
        print("__init__ of class B")
    def method1(self):
        super().method1()
        print("Always party")

b1 = B()
b1.method1()
b1.method()





