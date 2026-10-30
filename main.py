#eindopdracht
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text
import requests
from dotenv import dotenv_values
import json

WELCOME_MESSAGE = Text.from_markup("[bold red]WELCOME TO THE DINNERS CHOICE APP![/bold red]", justify="center")

print("[bold red]alert![/bold red] Something happened")

def show_main_menu():
    print("""
1. Favorite recipes
2. Blacklist
3. Find new recipes
0. Exit
""")

def show_favorites_menu():
    print("""
1. Show favorites
2. Remove recipe from favorites
3. Add recipe to favorites
0. Return to main menu
""")

def show_new_recipes_menu():
    print("""
1. Show 3 random recipes
2. Show 3 recipes by category
3. Show 3 recipes from favorites list
0. Return to main menu
""")

def show_blacklist_menu():
    print("""
1. Show blacklist
2. Add recipe to blacklist
3. Remove recipe from blacklist
0. Return to main menu
""")


def main():
    print(Panel.fit(WELCOME_MESSAGE))
    while True:
        show_main_menu()
        user_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "0"])
        match user_choice:
            case "1":
                show_favorites_menu()
                user_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "0"])
                match user_choice:
                    case "1":
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
                    case "0":
                        pass
            case "2":
                show_blacklist_menu()
                user_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "0"])
                match user_choice:
                    case "1":
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
                    case "0":
                        pass
            case "3":
                show_new_recipes_menu()
                user_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "0"])
                match user_choice:
                    case "1":
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
                    case "0":
                        pass
            case "0":
                #print exit message
                exit(0)


main()