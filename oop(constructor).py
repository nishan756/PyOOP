class student:
    def __init__(self):
        print("Nishan")
        print("Nishan is created")

s1 = student()

# ------------------------------------

class std:
    def __init__(self,name,group,id):
        self.Name = name
        self.Group = group
        self.Id = id
        self.department = "CSE"
        print(self.Name,self.Group,self.Id,self.department)
s1 = std("Nishan","A",853756)
s2 = std("Shakib","A",853750)

# ---------------------------------------------

class triangle:
    def __init__(self,x,y,z):
        self.A = x
        self.B = y
        self.C = z
    def area(self):
        print("Area =",self.A*self.B*self.C)
t1 = triangle(2,8,7)
t2 = triangle(1,5,8)
t1.A = 4
t1.area()
t2.area()

# --------------------------------------------------

class house:
    def __init__(self):
        self.window = 4
        self.door = 3
        self.corridor = 2

    def view(self):
        print("Windows =",self.window,"Doors =",self.door,"Corridor =",self.corridor)
h1 = house()
h1.view()
h1.window = 6
h1.view()  

# ------------------------------------------------

class car:
    def __init__(self,name,model,color):
        self.name = name   #instance variable
        self.model = model  #instance variable
        self.color = color  #instance variable
        self.wheel = 4
    def detail(self): #instance method
        print("Name:",self.name,"Model:",self.model,"Color:",self.color)
c1 = car("BMW",2016,"Red")
c1.detail()
c2 = car("Audi",2018,"Black")
c2.detail()
c2.color = str(input("Input:"))
c2.detail()

# -----------------------------------------------------

class dog:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def update_color(self,color):
        self.color = color
    def poke(self):
        print("The dog name is",self.name,"and color is",self.color)

d1 = dog("Tommy","Brown")
d2 = dog("Robert","White")
d1.poke()
d2.poke()
d1.update_color("Black")
d1.poke()
d2.update_color("Red")
d2.poke()

print(d1.__dict__) 

print(dir(d1))

# ---------------------------------------

class book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
        self.price = 0
    def uppri(self,price):
        self.price = price
    def view(self):
        print(f"Book-Name: {self.name}\nAuthor: {self.author}\nPrice: {self.price}")
b1 = book("Shuvro","Humayun Ahmed")
b2 = book("Opekkha","Humayun Ahmed")
b1.uppri(150)
b2.uppri(225)
b1.view()
print("--------------")
b2.view()

# -----------------------------------------------

#pass by reference 
class cat:
    def __init__(self,color,action):
        self.color = color
        self.action = action
    def view(self):
        print(self.color,"cat is",self.action)
    def update_color(self,color):
        self.color = color
    def update_action(self,action):
        self.action = action
    def compare(self,cat):
        if self.action == cat.action and  self.color == cat.color:
            print("Both cat looks same and they are",self.action)
        elif self.color != cat.color and self.action == cat.action:
            print("Different color cats are",self.action)
        elif self.action != cat.action and self.color == cat.color:
            print("colr matched")
        else:
            print("They are fully different")
c1 = cat("Black","Jumping")
c2 = cat("White","Sitting")
c3 = cat("Black","Jumping")    
c1.view()
c2.view()
c1.compare(c2)
c2.compare(c3)
c1.compare(c3)
c1.update_action("Walking")
c1.compare(c3)
c2.update_color("Brown")
c2.compare(c3)
c1.compare(c3)

# -------------------------------------------------

class Student:
    def __init__(self,name,group,roll,GPA):
        self.name = name
        self.group = group
        self.roll = roll
        self.gpa = GPA
    def update_gpa(self,GPA):
        self.gpa = GPA
    
    def update_group(self,group):
        self.group = group
    def compare(self,std):
        if self.gpa > std.gpa:
            print("s1 is more good than s2")
        elif self.gpa == std.gpa:
            print("They are same")
        else:
            print("S2 is more good tham s1")
    
    def view(self):
        print(f"Name:{self.name}\nRoll:{self.roll}\nGroup:{self.group}\nGPA:{self.gpa}")
std1 = Student("Nishan","A",853756,5.00)
std1.view()
std1.update_gpa(4)
std1.update_group("C")
std1.view()
std2 = Student("Nahid","A",853757,4.5)
std1.compare(std2)
# -------------------------------------------------

# pass by value and pass by reference

# ex-1

class addition:
    def __init__(self,color,num):
        self.num = num
        self.color = color
    def view(self,num,clr):
        num += 5
        clr[0] = "Green"
        print("Method inside",num)
        print("Method inside",clr)
# # -------------------------------------------
x = 45
color = ["Red","Yellow","Black","Indigo"]
c1 = addition(x,color)
c1.view(x,color)
print("Method outside",x)
print("Method outside",color)

# ------------------------------------------------
# ex-2

class numlist:
    def __init__(self,num,list):
        self.num = num
        self.list = list
    def multiplication(self,num,lst):
        num *= 5
        lst[0] = 8
        print("Method inside",num)
        print("Method inside",lst)

num1 = 15
numberlist = [0,1,2,3,45,6,7,8,9,10]
l1 = numlist(num1,numberlist)
l1.multiplication(num1,numberlist)
print("Method outside",num1)
print("Method outside",numberlist)

# -----------------------------------------------------------

class dog:
    def __init__(self,name,color,action):
        self.name = name
        self.color = color
        self.action = action

    def compare(self,cat):
        if self.action == cat.action and self.color == cat.color:
            print(f"They are same and they are {self.action}")

        elif self.action == cat.action and self.color != cat.color:
            print(f"They looks different and they are {self.action}")

        elif self.action != cat.action and self.color == cat.color:
            print("They are same and their action is different")

    def view(self):
        print(f"Dog Info\nName:{self.name}\nColor:{self.color}\nAction{self.action}")

d1 = dog("Tommy","white","Laughing")
d2 = dog("Doggy","white","Running")
d3 = dog("Doggy","Black","Crying")
d1.compare(d2)
d1.compare(d3)

# ----------------------------------------------

# pass by value and pass by reference
# -----------------------------------
class add:
    def __init__(self,num,color):
        self.num = num
        self.color = color

    def view(self,num,color):
        num+=5
        color[0] = "Green"
        print("method-inside",num)
        print("method-inside",color)

num = 15
color = ["Blue","Yellow","White"]
add1 = add(num,color)
add1.view(num,color)

print("method-outside",num)  #pass by value
print("method-outside",color) #pass by reference




















        
    