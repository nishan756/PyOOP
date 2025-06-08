# single inheritence
# ------------------
class animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def eat(self):
        print(self.color,self.name,"is eating")

class dog(animal):
    def bark(self):
        print(self.color,self.name,"is barking")

a1 = animal("ZACK","White")
d1 = dog("Rovert","Black")
d1.bark()
d1.eat()
print(isinstance(animal,dog))

# multiple inheritence
# --------------------

class A:
    def __init__(self):
        print("__init__ of class A")
    def mmethod1(self):
        print("Method1 of class A")

class B:
    def __init__(self):
        print("__init__ of class B")

    def method2(self):
        print("Method2 of class B")

class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("__init__ of class C")
    def method3(self):
        print("method3 of class C")


c1 = C()
c1.mmethod1()
B.method2(c1)
A.mmethod1(c1)

# ---------------------------------------------------------

# Variable overriding
# -------------------
class Animal:
    def __init__(self,name):
        self.name = name
        self.color = "White"
    def eat(self):
        print(self.color,self.name,"is eating")

class dog(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color
    def bark(self):
        print(self.color,self.name,"is barking")

d1 = dog("Robert","Black")
d1.bark()
d1.eat()












class father:
    car = "Aston-Martin"
    house = ""
    phone = "Huawei"

class mother:
    gold_chain = "24carat"
    ring = "Diamond"
    phone = "Samsung"

class child1(mother,father):  #multiple inheritence
    phone = "Honor"

ch1 = child1()
print(ch1.car,ch1.gold_chain,ch1.phone)

# ----------------------------------------------------------

# multilevel inheritence  #the last one can use each and everything
# ----------------------
class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def output(self):
        print(f"Name:{self.name}\nId:{self.id}")

class csestudent(student):
    def __init__(self,name,id,labs):
        super().__init__(name,id)
        self.No_of_labs = labs
    
    def see(self):
        print("Name:",self.name,"\nId:",self.id,"\nNumber of Lab:",self.No_of_labs)

class csefresher(csestudent):
    def enroll(self):
        print(self.see(),"\nEnroll CSE110")

cs1 = csestudent("bob",853756,3)
cs1.see()
cs2 = csefresher("Nishan",853756,3)
cs2.output()

# -------------------------------------------------



class father:
    house = "5floor"
    watch = "Tissot"
    phone = "Samsung"
    car = "Range-Rover"
class mother(father):
    gold = "24carat"
    # diamond = ""

class child1(mother):
    car1 = "BMW"

class child2(child1):
    car2 = "Marcedes"

class child3(child2):
    car3 = "Ferrari"

chl1 = child3()
print(chl1.car,chl1.car1,chl1.car2,chl1.car3)
chl2 = child2()
print(chl2.car2)

# -----------------------------------------------------------------
# Hybrid inheritence (mix inheritence)
# ------------------------------------------

class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def details(self):
        print(f"Name:{self.name}\nId:{self.id}")

class cse(student):
    def __init__(self,name,id,labs):
        super().__init__(name,id)
        self.No_of_labs = labs
    def view(self,labs):
        self.No_of_labs = labs
        print(self.details(),"\nLab:",self.No_of_labs)

class eee(cse):
    pass

class BBA(student):
    def party(self):
        print(self.details(),"\nAll day party")

cs1 = cse("Nishan",853756)
cs1.view(5)

ee1 = eee("Nahid",853750)
ee1.view(3)

bb1 = BBA("Nahid",454545)
bb1.party()

print(help(cs1))


# --------------------------------------------------------------------

# Hierarchical inheritence 
# ------------------------------------

class grandclass:
    def method1(self):
        print("This is method-1")
class parentclass(grandclass):
    def method2(self):
        print("This is method-2")
class child1(parentclass):
    def method3(self):
        print("This is method-3")    

class child2(child1):
    def method4(self):
        print("This is method-4")


ch1 = child2()
ch1.method3()
# --------------------------------------------------------


class monster:
    def __init__(self,name,minute):
        self.name = name
        self.color = "Black"
        self.minute = minute
    def attack(self):
        print(f"{self.color} {self.name} will attack within {self.minute} minutes")
    

class monster1(monster):
    def __init__(self,name,color,head,noes,canfly):
        super().__init__(name,color)
        self.head = head
        self.noes = noes
        self.fly = canfly
        self.color = color

    def Attack(self):
        if self.fly == "Yes":
            print(f"I have{self.head} head and {self.noes} noses.I can fly and I'am coming to attack you")

        else:
            print(f"I have {self.head} head and {self.noes} noses. I'am coming to attack you")
    def makesound(self):
        print("Hiiissssshhhh")
class monster2(monster):
    
    def __init__(self,name,color,minute):
        super().__init__(name,minute)
        self.color = color
        self.heads = 5
        self.hands = 10
        self.leg = 3
        self.wing = 5
        self.minute = 0

    def seeme(self):
        
        print(f"{self.name} has:\nHead:{self.heads}\nHand:{self.hands}\nLeg:{self.leg}\nWIng:{self.wing}\nColor: {self.color} skin") 

mon3 = monster2("Tangleface","White",0)
mon3.seeme()
print(" ")
mon1 = monster("mournsnake","15")
mon1.attack()
print(" ")
mon2 = monster1("fogthing","Ash",2,2,"No")
mon2.Attack()
mon2.makesound()

# ----------------------------------------------------

class fdog:
    def __init__(self,name):
        self.name = name
        self.color = "White"

    def view(self):
        print(f"Dog-Name:self{self.name}\nColor:{self.color}")

    def eat(self):
        print(self.color,self.name,"drinking water")

class mdog(fdog):
    def __init__(self,name):
        super().__init__(name)
        self.color = "Brown"
class bdog(mdog):
    def bark(self):
        print(self.color,self.name,"barking")

class gdog(fdog):
    def bark(self):
        print(self.color,self.name,"barking")

d1 = bdog("Tommy")
d1.eat()
d1.bark()

d2 = gdog("Lucy")
d2.eat()
