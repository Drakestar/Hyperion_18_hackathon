import random


def get_profession():
    return (random.choice(open("./GenFiles/professions.txt", "r").readlines())).replace("\n", "")
