class student:
    def __init__(self,name,id):
        self.name = name
        self.__id = id

    def details(self):
        self.__method()
        print("Name:",self.name,"Id:",self.__id)

    def __method(self):
        print("private method executed")

s1 = student("Nishan",853756)
s1.details()