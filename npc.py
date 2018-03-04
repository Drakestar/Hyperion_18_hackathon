import nameGen
import random
import professionGen

# Class for npc that sets as base values before being adjusted
class Npc:
    gender = "male"
    name = "name"
    age = 1
    max_age = 65
    profession = "child"

    def __init__(self):
        self.gender = random.choice(["Male", "Female"])
        if self.gender == "Male":
            self.name = nameGen.get_full_name_human_male()
        else:
            self.name = nameGen.get_full_name_human_female()
        self.age = random.randint(0, 65)
        self.max_age = 65
        if self.age < 1:
            self.profession = "infant"
        elif self.age < 10:
            self.profession = "child"
        else:
            self.profession = professionGen.get_profession()

    def __str__(self):
        return self.name + ", " + self.gender + ", " + str(self.age) + ", " + self.profession

    def age(self, years: int):
        self.age += years
        if self.age > self.max_age:
            return self.die()

    def die(self):
        self.name = "The Deceased, " + self.name
        return 1
