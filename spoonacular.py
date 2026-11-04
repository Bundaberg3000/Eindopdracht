from my_secret import API_KEY
import requests
from rich import print
import json
import list_functions
from rich.prompt import Prompt
from rich.table import Table
import logging

logger = logging.getLogger(__name__)


def handle_response(response):
    """Check de response code en filter de info met get_recipe_and_id()
    geef de gefilterde info terug"""
    if  response.ok:
        data = response.json()
        user_dict = get_recipe_and_id(data)
        return user_dict
    else:
        print(f"Error: {response.status_code} - {response.text}")
        logging.error(f"Fout: {response.status_code} - {response.text}")
        return None

def get_random_recipes(category=None):
    """de call naar de random recipe endpoint maken evt. met category.
    Met een handle_response voor de status check en filteren data. Geeft de dict terug"""
    random_url = "https://api.spoonacular.com/recipes/random"
    if category is None:
        try:
            response = requests.get(f"{random_url}?apiKey={API_KEY}&include-tags=main course&number=3")
        except requests.ConnectionError:
            print("Er lijkt geen verbinding met het internet te zijn...")
            logging.error("Connection error")
            return None
        else:
            user_dict = handle_response(response)
            return user_dict
    else:
        try:
            response = requests.get(f"{random_url}?apiKey={API_KEY}&number=3&include-tags=main course,{category}")
        except requests.ConnectionError:
            print("Er lijkt geen verbinding met het internet te zijn...")
            logging.error("Connection error")
            return None
        else:
            user_dict = handle_response(response)
            return user_dict


def get_recipe_and_id(data):
    """ De informatie die we willen gebruiken filteren uit de response
    en terug geven in een dict object"""
    user_number = 1
    user_dict = {}
    for recipe in data["recipes"]:
        recipe_id = recipe["id"]
        recipe_title = recipe["title"]
        user_dict[user_number] = {recipe_id:recipe_title}
        user_number += 1
    return user_dict

def user_picks_recipe(user_data):
    """Door het dict loopen, checken of de recepten al in favorites of blacklist staan
    en anders de recepttitels genummerd weergeven om de gebruiker een keuze te kunnen
    laten maken. We geven de titel terug en ook achter de schermen het ID-nummer wat we
    nodig hebben voor de volgende calls"""
    if user_data is None:
        return None
    for key_number, recipe_info in user_data.items():
        for recipe_id in recipe_info:
            recipe_name = recipe_info[recipe_id]
            if list_functions.check_for_in_list(recipe_id, "favorites"):
                print(f"{key_number}: {recipe_name} (Already in favorites.)")
            elif list_functions.check_for_in_list(recipe_id, "blacklist"):
                print(f"{key_number}: {recipe_name} (RECIPE IS ON BLACKLIST).")
            else:
                print(f"{key_number}: {recipe_name}")
    print("0: I dont like these choices, get me out of here!")
    print()
    user_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "0"])
    if user_choice == "0":
        return None, None
    else:
        chosen_item = user_data[int(user_choice)]
        for recipe_id, recipe_name in chosen_item.items():
            picked_title = recipe_name
            picked_id = recipe_id
        return picked_title, int(picked_id)


def get_recipes(category):
    """ extra functie om main beter leesbaar te houden"""
    chosen_title, chosen_id = user_picks_recipe(get_random_recipes(category))
    return chosen_title, chosen_id


def get_ingredients(chosen_id):
    """call naar het ingrediënten endpoint met show_ingredients() voor het weergeven."""
    ingredients_url = f"https://api.spoonacular.com/recipes/{chosen_id}/ingredientWidget.json"
    try:
        response = requests.get(f"{ingredients_url}?apiKey={API_KEY}")
    except ConnectionError:
        print("Er lijkt geen verbinding met het internet te zijn...")
        logging.error("Connection error")
    else:
        if response.ok:
            data = response.json()
            show_ingredients(data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            logging.error(f"Fout: {response.status_code} - {response.text}")


def get_instructions(chosen_id):
    """call naar het instructions endpoint met show_instructions voor het weergeven."""
    instructions_url = f"https://api.spoonacular.com/recipes/{chosen_id}/analyzedInstructions"
    try:
        response = requests.get(f"{instructions_url}?apiKey={API_KEY}")
    except ConnectionError:
        print("Er lijkt geen verbinding met het internet te zijn...")
        logging.error("Connection error")
    else:
        if response.ok:
            data = response.json()
            show_instructions(data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            logging.error(f"Fout: {response.status_code} - {response.text}")


def show_ingredients(data):
    """het vormgeven van een table om de ingrediënten genummerd weer te geven
    en her weergeven zelf"""
    table = Table(title="TODAY'S RECIPE")
    table.add_column("Ingredient", justify="right", style="cyan", no_wrap=True)
    table.add_column("Amount", style="magenta")
    table.add_column("Unit", justify="right", style="green")

    for ingredient in data["ingredients"]:
        ingredient_name = ingredient['name']
        ingredient_amount = str(ingredient['amount']['metric']['value'])
        ingredient_unit = ingredient['amount']['metric']['unit']
        table.add_row(ingredient_name, ingredient_amount, ingredient_unit)
    print(table)

def get_ingredients_instructions(chosen_title, chosen_id):
    """deze is zodat ik dit niet 2 keer hoef te typen in het random recipes menu.
    """
    list_functions.add_to_list(chosen_title, chosen_id, "history")
    get_ingredients(chosen_id)
    input("Press enter to continue to instructions.....")
    get_instructions(chosen_id)


def show_instructions(data):
    """vormgeven van een tafel om de instructies genummerd weer te geven en
    het weergeven zel"""
    table = Table(title="TODAY'S STEPS", width=150)
    table.add_column("Step", justify="right", style="cyan", no_wrap=True)
    table.add_column("Instructions", style="magenta")
    for items in data:
        for steps in items['steps']:
            step_number = str(steps['number'])
            step_instruction = steps['step']
            table.add_row(step_number, step_instruction)
    print(table)













