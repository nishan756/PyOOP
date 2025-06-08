
class engine:
    def __init__(self,model,cc):
        self.model = model
        self.cc = cc

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")


class car:
    def __init__(self,name,model,cc):
        self.name = name
        self.engine = engine(model,cc)
    
    def  run(self):
        self.engine.start()
        print("Car is running")
c1 = car("BMW",3000,"M10")
c1.run()
c2 = car("Marcedes",2500,"M10")


    


        