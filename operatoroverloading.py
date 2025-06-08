class sum:
    def __init__(self,x,y):
        self.sum = x+y
        print(self.sum)

num1 = sum(10,20)
num2 = sum(20,30)
print(num1+num2)  #cant addition this because num1 and num2 is not int. 

# ---------------------------------------------------------------------

# overload
# --------

class sum:
    def __init__(self,x):
        self.x = x

    def __add__(self,other):
        return self.x + other.x

sum1 = sum(20)
sum2 = sum(20)
print(sum1.__add__(sum2))

# -----------------------------------------





