import random


# human name generators
def get_theme():
    return (random.choice(open("./GenFiles/storyThemes.txt", "r").readlines())).replace("<ALLY>", random.choice(
        open("./GenFiles/storyAlly.txt", "r").readlines())).replace("<ENEMY>", random.choice(
        open("./GenFiles/storyEnemy.txt", "r").readlines())).replace("<ITEM>", random.choice(
        open("./GenFiles/storyItem.txt", "r").readlines())).replace("\n", "")


def get_hook():
    return (str(random.choice(open("./GenFiles/storyHooks.txt", "r").readlines()))).replace("\n", "")
