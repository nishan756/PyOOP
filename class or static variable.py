# Example-1
# ---------

class player:
    team_run = 0
    def __init__(self,run):
        self.run = run
    
    def hit_four(self):
        self.run += 4
        player.team_run += 4

    def hit_six(self):
        self.run += 6
        player.team_run += 6

    
sakib = player(0)
sakib.hit_four()
sakib.hit_six()
tamim = player(0)
tamim.hit_four()
tamim.hit_six()
print("Sakib:",sakib.run)
print("Tamim:",tamim.run)
print("Team-RUn:",player.team_run)
# -----------------------------------------------------------

# Example-2
# ---------

class student:
    counter = 0
    def __init__(self,name,id):
        self.name = name
        self.id = id
        student.counter += 1

    def details(self):
        print("Name:",self.name,"\nId:",self.id)

print(student.counter)
s1 = student("Nishan",853756)
s2 = student("Abir",853750)
s3 = student("Israfil",858585)
print(student.counter)
# -------------------------------------------------------
