class Parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
blu = Parrot("Blu",10)
aerodyanamicness = Parrot("Aerodynamicness",15)

print("blu is a {}".format(blu.species))
print("aerodynamicness is a {}".format(aerodyanamicness.species))

blu = print("{},is {}".format(blu.name,blu.age))
aerodyanamicness = print("{},is {}".format(aerodyanamicness.name,aerodyanamicness.age))