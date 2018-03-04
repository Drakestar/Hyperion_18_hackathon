import nameGen
import random


class Npc:
    gender = "male"
    name = "name"
    age = 1

    def __init__(self):
        self.gender = random.choice("Male", "Female")
        if self.gender == "Male":
            self.name = nameGen.get_full_name_human_male()
        else:
            self.name = nameGen.get_full_name_human_female()
        self.age = random.randint() % 65
