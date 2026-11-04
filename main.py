#eindopdracht
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
import spoonacular
import list_functions
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

WELCOME_MESSAGE = Text.from_markup("WELCOME TO THE DINER'S CHOICE APP!", justify="center")
EXIT_MESSAGE = Text.from_markup("THANKS FOR USING THE DINER'S CHOICE APP. HAPPY COOKING AND BON APPETIT!")

def show_main_menu():
    print("""
1. Favorite recipes
2. Blacklist
3. Find random recipes menu
0. Exit
""")

def favorites_menu():
    while True:
        print("""
1. Show favorites
2. Remove recipe from favorites
3. Add recipe to favorites
0. Return to main menu
""")
        user_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "0"])
        match user_choice:
            case "1":
                list_functions.show_list("favorites")
            case "2":
                list_functions.show_list("favorites")
                print()
                list_functions.remove_from_list_input("favorites")
            case "3":
                list_functions.show_list("history")
                print()
                list_functions.add_to_list_input("favorites")
            case "0":
                return


def show_random_recipes_menu():
    while True:
        print("""
1. Show 3 random recipes
2. Show 3 recipes by category
3. Show 3 recipes from favorites list
0. Return to main menu
""")
        user_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "0"])
        print()
        match user_choice:
            case "1":
                chosen_title, chosen_id = spoonacular.get_recipes(category=None)
                if chosen_title is None:
                    return
                spoonacular.get_ingredients_instructions(chosen_title, chosen_id)
            case "2":
                user_choice = Prompt.ask("Enter your choice", choices=["fish", "meat", "vegetarian"])
                chosen_title, chosen_id = spoonacular.get_recipes(user_choice)
                if chosen_title is None:
                    return
                spoonacular.get_ingredients_instructions(chosen_title, chosen_id)
            case "3":
                chosen_id = list_functions.pick_from_favorites()
                if chosen_id is None:
                    return
                spoonacular.get_ingredients(chosen_id)
                input("Press enter to continue to instructions.....")
                spoonacular.get_instructions(chosen_id)
            case "0":
                return

def blacklist_menu():
    while True:
        print("""
1. Show blacklist
2. Remove recipe from blacklist
3. Add recipe to blacklist
0. Return to main menu
""")
        user_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "0"])
        print()
        match user_choice:
            case "1":
                list_functions.show_list("blacklist")
            case "2":
                list_functions.show_list("blacklist")
                print()
                list_functions.remove_from_list_input("blacklist")
            case "3":
                list_functions.show_list("history")
                print()
                list_functions.add_to_list_input("blacklist")
            case "0":
                return


def main():
    print(Panel.fit(WELCOME_MESSAGE))
    while True:
        show_main_menu()
        user_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "0"])
        match user_choice:
            case "1":
                favorites_menu()
            case "2":
                blacklist_menu()
            case "3":
                show_random_recipes_menu()
            case "0":
                print(Panel.fit(EXIT_MESSAGE))
                exit(0)


main()