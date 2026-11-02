import json
from rich.panel import Panel
from rich.text import Text
from rich import print
import random


def show_list(list_name):
    """voor het weergeven van de verschillende list bestanden"""

    with open(f"stored lists/{list_name}.json", "r") as file:
        list_dict = json.load(file)
        print(Panel.fit(f"Here are your {list_name} recipes."))
        for index, item in enumerate(list_dict):
            print(index, item)


def add_to_list(clean_title, recipe_id, list_name):
    """voor het toevoegen van items aan de list bestanden"""

    with open(f"stored lists/{list_name}.json", "r") as file:
        list_dict = json.load(file)
        list_dict[clean_title] = recipe_id
        print(list_dict)
        with open(f"stored lists/{list_name}.json", "w") as file1:
            json.dump(list_dict, file1)


def remove_from_list(recipe_name, list_name):
    """voor het verwijderen van items van de lijst bestanden"""

    with open(f"stored lists/{list_name}.json") as file:
        list_dict = json.load(file)
        if recipe_name in list_dict:
            del list_dict[recipe_name]
            with open("stored lists/favorites.json", "w") as file1:
                json.dump(list_dict, file1)
        else:
            print(f"{recipe_name} not found in {list_name}!")


def check_for_in_list(recipe_id, list_name):
    """check om te zien of gesuggereerde recepten al in een van onze
    gebruikers lijsten staan"""

    with open(f"stored lists/{list_name}.json", "r") as file:
        list_dict = json.load(file)
        return recipe_id in list_dict.values()


def pick_from_favorites():

    """In this function i will use a while true loop for the choice instead
     of the prompt from RICH so i can show i know how to use try and except
     for validating and error handling"""

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






