
# class student:
#     def __init__(self,name,id):
#         self.name = name
#         self.__id = id

#     def view(self):
#         print(self.name,self.__id)

#     def update_id(self,id):
#         if id > 0:
#             self.__id = id
#         else:
#             print("Invalid id,ENter id again")


# s1 = student("Nishan",853756)
# s1.view()
# s1.update_id(333)
# s1.view()

# ------------------------------------------------

# getter-setter method
# --------------------
# class dog:
#     def __init__(self,name,color):
#         self.__name = name
#         self.__color = color

#     def view(self):
#         print(f"Dog-Name:{self.__name}\nDog-Color:{self.__color}")

#     def setcolor(self,color):
#         self.__color = color

#     def getcolor(self):
#         return self.__color
#     def setname(self,name):
#         self.__name = name
#     def getname(self):
#         return self.__name
    

# d1 = dog("Charlie","Black")
# d1.view()
# print(d1.getname())
# print(d1.getcolor())
# d1.__color = "White"
# print(d1.getcolor())
# print(d1.__dict__)

# ------------------------------------------------------

# class engine:
#     def __init__(self,cc):
#         self.__cc = cc

#     def start(self):
#         print("Engine Started")

#     def stop(self):
#         print("Engine Stopped")

# class aircraft:
#     def __init__(self,brand,name,cc):
#         self.engine = engine(cc)
#         self.__cc = cc
#         self.__name = name
#         self.__brand = brand

#     def about(self):
#         print(f"About Aircraft\nBrand:{self.__brand}\nName:{self.__name}\nCC:{self.__cc}")

#     def set_brand(self,brand):
#         self.__brand = brand
#     def get_brand(self):
#         return self.__brand
    
#     def set_name(self,name):
#         self.__name = name
#     def get_name(self):
#         return self.__name

#     def on(self):
#         self.engine.start()
#         print(self.__name,"started")
#     def run(self):
#         print(self.__name,"is running")

#     def takeoff(self):
#         print(self.__name,"is taking off")

#     def off(self):
#         self.engine.stop()
#         print("Aircraft is on the land")

# a1 = aircraft("Airbus","A380","4.8Million")
# a1.about()
# a1.on()
# a1.run()
# a1.takeoff()
# a1.off()
# a1.set_name("Beluga")
# print(a1.get_name())

# -------------------------------------------------------






    

