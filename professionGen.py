import random

# Picks a random profession from the text file in GenFiles
def get_profession():
    return (random.choice(open("./GenFiles/professions.txt", "r").readlines())).replace("\n", "")
