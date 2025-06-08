# """যখন একটা ক্লাসে সেম নাম ২টা মেথড 
# থাকে কিন্তু প্যারামিটার ভিন্ন তকে মেথড ওভারলোডিং বলে"""
class calculator:
    def product(self,num1,num2):
        print("product=",num1*num2)

    def product(self,num1,num2,num3):
        print(num1*num2*num3)

c1 = calculator()
c1.product(15,15,15)

# # ---------------------------------------------
class calculator:
    def product(self,num1,num2 = None,num3 = None):
        if num1 != None and num2 != None and num3 != None:
            print("Product =",num1*num2*num3)

        elif num1 != None and num2 != None and num3 == None:
            print("Product =",num1*num2)

        else:
            print("product =",num1)


a = calculator()
a.product(3)
a.product(3,3)
a.product(3,3,3)

# -----------------------------------------------------

class calculator:
    def product(self,*num):
        Sum = 1
        for i in num:
            Sum *= i

        print(Sum)

b = calculator()
b.product(4,5,8)

# -----------------------------------------------------

class add:
    def calculate(self,*num):
        sum = 0
        for i in num:
            sum += i

        print("Total:",sum)


add1 = add()
add1.calculate(4,8,9,96,3,3,6,8)