# class Engine:
#     def __init__(self,cc):
#         self.cc = cc

#     def start(self):
#         print("Engine started")


#     def stop(self):
#         print("Engine stopped")

# ---------------------------------------------------------------
# class car:
#     def __init__(self,name,cc):
#         self.engine = Engine(cc)
#         self.name = name

#     def run(self):
#         self.engine.start()
#         print("Car is running")


#     def Break(self):
#         self.engine.stop()
#         print("Car stopped")


# c = car("BMW",2000)
# c.run()
# c.Break()
# print(c)
# --------------------------------------------------------------------

# class jet:
#     def __init__(self,no_engine,cc):
#         self.jet = Engine(cc)
#         self.noengine = no_engine

#     def fly(self):
#         self.jet.start()
#         print("Jetplane is flying")

#     def land(self):
#         print("Jetplane landing")

#     def off(self):
#         self.jet.stop()
#         print("Jetplane is on land")

# j1 = jet(2,"9.6million")
# j1.fly()
# j1.land()
# j1.off()

# --------------------------------------------------------------------
# class helicopter:
#     def __init__(self,name,cc):
#         self.name = name
#         self.Jet = Engine(cc)

#     def on(self):
#             self.Jet.start()
#             print("Fan are rotating")
#     def off(self):
#             self.Jet.stop()
#             print("fan is off now")

#     def Fly(self):
#             self.on()
#             print(self.name,"is flying which has",self.Jet.cc,"engine")

#     def land(self):
#             self.off()
#             print(self.name,"is on land which has",self.Jet.cc,"engine")


# h1 = helicopter("Bell 206 Jet Ranger",15680)
# h1.Fly()
# h1.land()

# ----------------------------------------------------------------------





# --------------------------------------