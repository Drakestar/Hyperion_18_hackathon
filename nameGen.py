import random


# human name generators
# human names


def get_first_name_human_male():
    return (random.choice(open("./GenFiles/maleNames.txt", "r").readlines())).replace("\n", "")


def get_full_name_human_male():
    return (str(random.choice(open("./GenFiles/maleNames.txt", "r").readlines())) + " " + str(
        random.choice(open("./GenFiles/surnames.txt", "r").readlines()))).replace("\n", "")


def get_first_name_human_female():
    return (random.choice(open("./GenFiles/femaleNames.txt", "r").readlines())).replace("\n", "")


def get_full_name_human_female():
    return (str(random.choice(open("./GenFiles/femaleNames.txt", "r").readlines())) + " " + str(
        random.choice(open("./GenFiles/surnames.txt", "r").readlines()))).replace("\n", "")


def get_surname_name_human():
    return (random.choice(open("./GenFiles/surnames.txt", "r").readlines())).replace("\n", "")


# human cities
def get_city_name():
    return (random.choice(open("./GenFiles/historicCityNames.txt", "r").readlines())).replace("\n", "")


def get_civilization_name():
    return (random.choice(open("./GenFiles/civilizationNames.txt", "r").readlines())).replace("\n", "")
