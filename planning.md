wat moet het doen:

de applicatie is er om iemand te helpen kiezen wat te koken en een boodchappenlijstje te produceren.

het kan iemand laten kiezen uit 3 willekeurige gerechten die worden gesuggereerd
het kan favorieten opslaan en daar een willekeurige selectie uit tonen om uit te kiezen.
je kan een gerecht op de blacklist zetten zodat je als je het krijgt als suggestie wordt vermeld dat je het niet lekker vond.
je kan zelf gerechten zoeken op cattegorie
je kan de voedingswaarde van de gerechten laten berekenen

ik ga de volgende endpoints gebruiken:
https://api.spoonacular.com/recipes/random
https://api.spoonacular.com/recipes/findByIngredients

print formatted welcome message

menu options:
- favorites:(shows stored favorite recipes by title with options
to get recipe, get shopping list,
remove from favorites, back to main )

- blacklist:(shows stored blacklisted recipes
,with options to remove from list, 
or go back to main menu)

- random choices for tonight's dinner:
(show random new choices,random new by category,random from favorites 
back to main menu)

- search recipe by name

- calculate nutritional values for picked recipe.


- use rich print to color outputs and linout
- use rich prompt for prompts (Intprompt for ints)
- clean user input ( strip, lower)
- validate user input is a string/int
- validate user chooses one of the given options
if not make them type it again


favorites: