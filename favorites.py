favorites = {2345:"chicken meatballs", 45667:"pasta carbonara"}


def add_favorite(recipe_name, recipe_id):
    global favorites
    if recipe_id not in favorites:
        favorites[recipe_id] = recipe_name
    else:
        print("Recipe already in favorites")

def show_favorites():
    for key,value in favorites.items():
        print(value)

def remove_favorite(recipe_name):
    for i in list(favorites.keys()):
        if favorites[i] == recipe_name:
            del favorites[i]

def update_favorites_file():



remove_favorite("chicken meatballs")
show_favorites()