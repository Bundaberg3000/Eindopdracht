#eindopdracht
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text
import requests
from secrets import API_KEY
import spoonacular
import list_functions


WELCOME_MESSAGE = Text.from_markup("[bold red]WELCOME TO THE DINER'S CHOICE APP![/bold red]", justify="center")

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
                recipe_to_remove = input
                list_functions.remove_from_list(recipe_to_remove)
            case "3":
                pass
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
                clean_title = chosen_title.lower()
                list_functions.add_to_list(clean_title, chosen_id, "history")
                spoonacular.get_ingredients(chosen_id)
                input("Press enter to continue to instructions.....")
                spoonacular.get_instructions(chosen_id)
            case "2":
                pass
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
2. Add recipe to blacklist
3. Remove recipe from blacklist
0. Return to main menu
""")
        user_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "0"])
        print()
        match user_choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
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
                #print exit message
                exit(0)


main()