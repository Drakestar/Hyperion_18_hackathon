import random


# human name generators
# human names


def get_first_name_human_male():
    return (random.choice(open("./NameGenFiles/maleNames.txt", "r").readlines())).replace("\n", "")


def get_full_name_human_male():
    return (str(random.choice(open("./NameGenFiles/maleNames.txt", "r").readlines())) + " " + str(
        random.choice(open("./NameGenFiles/surnames.txt", "r").readlines()))).replace("\n", "")


def get_first_name_human_female():
    return (random.choice(open("./NameGenFiles/femaleNames.txt", "r").readlines())).replace("\n", "")


def get_full_name_human_female():
    return (str(random.choice(open("./NameGenFiles/femaleNames.txt", "r").readlines())) + " " + str(
        random.choice(open("./NameGenFiles/urnames.txt", "r").readlines()))).replace("\n", "")


def get_surname_name_human():
    return (random.choice(open("./NameGenFiles/surnames.txt", "r").readlines())).replace("\n", "")


# human cities
def get_city_name():
    return (random.choice(open("./NameGenFiles/historicCityNames.txt", "r").readlines())).replace("\n", "")


def get_civilization_name():
    return (random.choice(open("./NameGenFiles/civilizationNames.txt", "r").readlines())).replace("\n", "")
