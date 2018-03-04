import Civilization
import nameGen


def generate_civs(civ_number):
    civ_list = []
    for i in range(civ_number):
        civ_list.append(Civilization.Civilization(nameGen.get_civilization_name(), 20, []))

    for civ in civ_list:
        civ.holdings_list.append(Civilization.Holding(nameGen.get_city_name(),'village',20))
    return civ_list


def start_making_history(turns, civs):
    civilizations = generate_civs(civs)

    for i in range(turns):
        for civ in civilizations:
            civ.take_actions()

    for civ in civilizations:
        print('Name:',civ.name)
        print('Population:',civ.total_population)
        print('Number of holding:',len(civ.holdings_list))