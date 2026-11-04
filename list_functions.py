import json
from json import JSONDecodeError
from rich.panel import Panel
from rich import print
import random
import logging
import cowsay
logger = logging.getLogger(__name__)


def show_list(list_name):
    """voor het weergeven van de verschillende list bestanden"""
    try:
        with open(f"stored lists/{list_name}.json", "r") as file:
            list_dict = json.load(file)
            print(Panel.fit(f"Here are your {list_name} recipes."))
            for index, item in enumerate(list_dict):
                print(index, item)

    except FileNotFoundError:
        print("File not found...")
        logger.error("File not found")
    except JSONDecodeError:
        print("Error when loading file...")
        logging.error("Failed to parse JSON correctly", exc_info=True)


def add_to_list_input(list_name):
    """Voor het afhandelen van de input van het toe te voegen item"""
    id_to_add = None
    while id_to_add is None:
        print("Enter 0 to return to menu...")
        recipe_to_add = input(
            "Which recipe do you want to add? (Enter the name from the above list) : ").strip().lower()
        if recipe_to_add == "0":
            return
        id_to_add = get_id_from_history(recipe_to_add)
        if id_to_add is None:
            print("Input error...")
            print()
    add_to_list(recipe_to_add, id_to_add, list_name)
    print()
    print(f"Added {recipe_to_add} to {list_name}")
    print()


def add_to_list(chosen_title, recipe_id, list_name):
    """Voor het toevoegen van items aan de list bestanden
    en het normaliseren van de tekst. spoonacular levert zeer onregelmatige tekst aan"""
    try:
        with open(f"stored lists/{list_name}.json", "r") as file:
            list_dict = json.load(file)
            clean_title = chosen_title.lower()
            list_dict[clean_title] = recipe_id
            with open(f"stored lists/{list_name}.json", "w") as file1:
                json.dump(list_dict, file1)
    except FileNotFoundError:
        print("File not found...")
        logger.error("File not found")
    except JSONDecodeError:
        print("Error when loading file...")
        logging.error("Failed to parse JSON correctly", exc_info=True)


def get_id_from_history(chosen_recipe):
    """haalt het id nummer op uit de history file"""
    try:
        with open("stored lists/history.json", 'r') as file:
            history_dict = json.load(file)
            if chosen_recipe in history_dict.keys():
                return history_dict[chosen_recipe]
            else:
                return None
    except FileNotFoundError:
        print("File not found...")
        logger.error("File not found")
    except JSONDecodeError:
        print("Error when loading file...")
        logging.error("Failed to parse JSON correctly", exc_info=True)


def remove_from_list_input(list_name):
    """Voor het afhandelen van de input van het te verwijderen item"""
    input_valid = False
    while not input_valid:
        print("Enter 0 to return to menu...")
        recipe_to_remove = input(
            "Which recipe do you want to remove? (Enter the name from the above list) : ").strip().lower()
        if recipe_to_remove == "0":
            return
        input_valid = remove_from_list(recipe_to_remove, list_name)
        if input_valid is None:
            print()
            print("Input error, please type a name from the list...")
            print(f"{recipe_to_remove} not removed!")
            print()
    print()
    print(f"{recipe_to_remove} removed from {list_name}")
    print()

def remove_from_list(recipe_name, list_name):
    """voor het verwijderen van items van de lijst bestanden
    met 2 checks om te zorgen dat de lijst bestanden de benodigde
    minimum aantal items behouden en te controleren of de input
    van de user klopt"""
    try:
        with open(f"stored lists/{list_name}.json") as file:
            list_dict = json.load(file)
            if list_name == "favorites":
                if len(list_dict) < 4:
                    print()
                    print("Can't remove more items. List must contain 3 items minimum")
                    print()
                    return False
            elif list_name == "blacklist":
                if recipe_name == "banaan":
                    cowsay.fox("THE BANAAN IS ETERNAL!")
                    print("Banaan not removed...")
                    return False
            if recipe_name in list_dict:
                del list_dict[recipe_name]
                with open(f"stored lists/{list_name}.json", "w") as file1:
                    json.dump(list_dict, file1)
                return True
            else:
                print()
                print(f"{recipe_name} not found in {list_name}!")
                return None

    except FileNotFoundError:
        print("File not found...")
        logger.error("File not found")
    except JSONDecodeError:
        print("Error when loading file...")
        logging.error("Failed to parse JSON correctly", exc_info=True)


def check_for_in_list(recipe_id, list_name):
    """check om te zien of gesuggereerde recepten al in een van onze
    gebruikers lijsten staan"""
    try:
        with open(f"stored lists/{list_name}.json", "r") as file:
            list_dict = json.load(file)
            return recipe_id in list_dict.values()

    except FileNotFoundError:
        print("File not found...")
        logger.error("File not found")
    except JSONDecodeError:
        print("Error when loading file...")
        logging.error("Failed to parse JSON correctly", exc_info=True)


def pick_from_favorites():

    """hier halen we 3 random keys(namen) op uit favorites
    om er daar 1 van te laten kiezen en van die keuze halen we vervolgens
    weer het recipe ID-nummer op om daarmee weer API calls te kunnen maken
    """
    try:
        with open("stored lists/favorites.json") as file:
            favorites = json.load(file)
            random_keys = random.sample(list(favorites), 3)
            dict_for_choice = {key: favorites[key] for key in random_keys}
            for counter, key in enumerate(dict_for_choice, start=1):
                print(f"{counter}: {key}")
            print("0: I dont like these recipes, get me out of here!")
            print()
            while True:
                try:
                    choice = int(input("Make your choice (0-3): "))
                    if 0 <= choice <= 3:
                        break
                    print("Enter a valid number..")

                except ValueError:
                    print("Input incorrect, please input a number (0-3).")
            if choice == 0:
                return None
            selected_recipe = random_keys[choice - 1]
            recipe_id = dict_for_choice[selected_recipe]
            return recipe_id

    except FileNotFoundError:
        print("File not found...")
        logger.error("File not found")
    except JSONDecodeError:
        print("Error when loading file...")
        logging.error("Failed to parse JSON correctly", exc_info=True)
