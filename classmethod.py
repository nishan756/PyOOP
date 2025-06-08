 class student:

     institution_name = "DPI"
    
     def __init__(self,name,id):
         self.name = name
         self.__id = id
     def details(self):
         print("Name:",self.name,"\nId:",self.__id,"\nCollege:",student.institution_name)

     @classmethod
     def update_clg(cls,clg):
         cls.institution_name = clg


 s1 = student("Nishan",853756) 
 s1.details()
 student.update_clg("Dhaka Polytechnic Institute")
 s1.details()

# -------------------------------------------------

 class student:
     institute = "DPI"
     def __init__(self,name,id):
         self.name = name
         self.__id = id


     def upid(self,id):
         self.__id = id

     @classmethod
     def upins(cls,institute):
         cls.institute = institute

     def details(self):
         print(f"Name:{self.name}\nId:{self.__id}\nInstitute:{student.institute}")
     @classmethod
     def string(cls,info):
         name,__id = info.split("-")
         obj = cls(name,__id)
         return obj
    
 s1 = student("Nishan",56)
 student.upins("Dhaka Polytechnic Institute")
 s1.details()
# # ------------------------------------------
 s1 = student.string("Nishan-58")
 s1.upid(60)
 s1.details()

 --------------------------------------------------------

# class student:
#     Institute = "DPI"
#     def __init__(self,name,id,sec):
#         self.name = name
#         self.__id = id
#         self.__sec = sec

#     def details(self):    #instance-method
#         print(f"Name:{self.name}\nSection:{self.__sec}\nId:{self.__id}\nInstitution:{student.Institute}")

#     def upid(self,id):
#         self.__id = id

#     def upsec(self,sec):
#         self.__sec = sec

#     @classmethod
#     def upinst(cls,Institute):
#         cls.Institute = Institute

#     def upid(self,id):
#         self.__id = id

#     @classmethod
#     def from_str(cls,info):
#         name,__id,sec = info.split("-")
#         obj = cls(name,__id,sec)
#         return obj

# # s1 = student("Bob",50,"A")
# # student.upinst("Dhaka Polytechnic Institute")
# # # s1.upid(60)
# # s1.details()

# s2 = student.from_str("Nishan-80-C")
# s2.details()

# print(s2.__dict__)
# -----------------------------------------------------

# class engine:
#     __brand = "BMW"
#     def __init__(self,name,cc):
#         self.__name = name
#         self.__cc = cc

#     def details(self):
#         print(f"Brand:{self.__brand}\nName:{self.__name}\nCC:{self.__cc}")

#     def upname(self,name):
#         self.__name = name

#     @classmethod
#     def upbrand(cls,brand):
#         cls.__brand = brand

#     @classmethod
#     def from_str(cls,info):
#         __name,__cc = info.split("-")
#         obj = cls(__name,__cc)
#         return obj

# class car:
#     def __init__(self,name,cc):
#         self.engine = engine(name,cc) 


# c1 = car("M4",1500)
# c1.engine.details()
# c1.engine.upbrand("Marcedes")
# c1.engine.details()
# c1.engine.upname("CLS")
# c1.engine.details()
# c2 = engine.from_str("X-1800")
# c2.upbrand("VOLVO")
# c2.details()
# -----------------------------------------------------------------



    


