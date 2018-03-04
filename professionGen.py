import random


def get_profession():
    return (random.choice(open("./GenFiles/maleNames.txt", "r").readlines())).replace("\n", "")