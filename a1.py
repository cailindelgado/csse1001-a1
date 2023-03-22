"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

def num_hours() -> float:
    return 11.42477796077

# Fill these in with your details
__author__ = "Cailin H Delgado"
__email__ = "c.delgado@uqconnect.edu.au"
__date__ = "03/03/2023"

from constants import *

def get_recipe_name(recipe: tuple([str, str])) -> str:
    """Returns the name of the recipe.
        get_recipe_name('chocco banana milkshake', '1.3 bananas')
    >> 'chocco banana milkshake'
    """
    return recipe[0]

def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
    """Returns the ingredient breakdown from the details amount, measure and ingredient.
    """
    bits = raw_ingredient_detail.split(" ")
    details_of_ingredients = (float(bits[0]), bits[1], " ".join(bits[2:])) 
    return details_of_ingredients
    
def create_recipe() -> tuple[str, str]:
    """Returns the recipe in the tuple[str, str] format after a series of prompting. 
       The recipe name is prompted first followed by continuous ingredient prompting
       until an empty string is returned. 
    """
    recipe_name = input("Please enter the recipe name: ")
    recipe_list = [recipe_name]
    recipe_ingredients, recipe_final_ingredients = "", ""
    while True:
        recipe_ingredient = input("Please enter an ingredient: ")
        if recipe_ingredient == "" or recipe_ingredient == " ":
           recipe_final_ingredients = recipe_ingredients[:-1] 
           break
        else:
            recipe_ingredients += recipe_ingredient.strip() + ','
            
    recipe_list.append(recipe_final_ingredients)
    return tuple(recipe_list)

def recipe_ingredients(recipe: tuple[str, str]) -> tuple[tuple[float, str, str]]:
    """Returns the ingredients of a recipe amount, measure and ingredient. This transforms 
       a given recipe from the string form into the tuples form.
    """
    recipe_details = str(recipe[1])
    recipe_ingredients_details = recipe_details.split(",")
    ingredient_breakdown = [] # list[tuple[float, str, str]]
    for num in range(0, len(recipe_ingredients_details)):
        ingredient_breakdown.append(parse_ingredient(recipe_ingredients_details[num]))
    return tuple(ingredient_breakdown)

def add_recipe(new_recipe: tuple[str, str], recipes: list[tuple[str, str]]):
    """Add a given recipe, new_recipe, into the list of recipes.
       Hint: this function doesn't return anything  """
    recipes.append(new_recipe)
#NOTE test this func

def find_recipe(recipe_name: str, recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
    """This function find and returns a recipe with a given recipe_name if it cannot be found returns None 
    """
    check_for_similarity_counter = 0  
    for item in recipes:
        if recipe_name not in item:
            check_for_similarity_counter += 1 
    
    if check_for_similarity_counter == len(recipes):
        return None

    for pos, item in enumerate(recipes):
        if recipe_name in item: 
           return recipes[pos]

def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    """remove a recipe from the list of recipes given the name of a recipe. If the recipe 
       name doesn't match any of the recipes withing the list of recipes then nothing happens
    """
    for pos, recipe in enumerate(recipes):
        if name in recipe:
            recipes.pop(pos)
    print(tuple(recipes))
#NOTE come back to this later, why doesnt assert work

def get_ingredient_amount(ingredient: str, recipe: tuple[str, str]) -> tuple[float, str] | None:
    """Return the amount and measure of a certain ingredient as a tuple[float, str] given an ingredient name 
       as a str and a recipe. If the ingredient doesnt exist then nothing happens
    """
    if ingredient in recipe[1]:
        bits = recipe[1].split(" ", 2)
        return float(bits[0]), bits[1]
#BUG if the ingredient is in the middle of the recipe, program wont work

def add_to_shopping_list(ingredient_details: tuple[float, str, str], shopping_list: list[tuple[float, str, str] | None]) -> None:
    """Add an ingredient to the shopping list which could either be empty or contain tuples of ingredient details. If the 
       ingredient being added already exists within the list then the amount should be combines. If the ingredient doesn't exist
       then it can be added without any calculations.

       It is assumed that the measure is consistent for all ingredients of the same name. In addition, ingredient_details contains 
       all the information about the ingredient being added to the shopping list. Also, the order doesn't matter. 
    """
    shopping_list_copy = shopping_list.copy()
    check = True
    if shopping_list == []:
        shopping_list.append(ingredient_details)
    else: 
        for ingredient in shopping_list_copy:
            for char in ingredient:
                if char == ingredient_details[2]:
                    list_recipe = list(ingredient)
                    new_amount = list_recipe[0] + ingredient_details[0]
                    list_recipe.insert(0, new_amount)
                    list_recipe.pop(1)
                    shopping_list.pop(0)
                    shopping_list.insert(0, list_recipe)
                    check = True
                elif char != ingredient_details[2]:
                    check = False

        if check == False:
            shopping_list.append(ingredient_details)

def remove_from_shopping_list(ingredient_name: str, amount: float, shopping_list: list) -> None:
    """Remove a certain amount of an ingredient, with the given ingredient_name, from the shopping list. If the ingredient exists in the shopping_list
       then the amount given as the parameter of this function should be subtracted from the amount that exists in the shopping_list. The ingredient should 
       be removed from the shopping list altogether if the amount goes below 0.
    """
    #NOTE doesnt say i have to remove the item if its amount hits 0
    shopping_list_copy = shopping_list.copy()
    if shopping_list == []:
        return None
    else: 
        for pos, item in enumerate(shopping_list_copy):
            if ingredient_name == item[2] and (amount >= item[0] or amount == item[0]):
                shopping_list.pop(pos)
            elif ingredient_name == item[2]:
                list_recipe = list(item)
                shopping_list.pop(pos)
                new_amount = list_recipe[0] - amount
                list_recipe.insert(0, new_amount)
                list_recipe.pop(1)
                shopping_list.insert(0, tuple(list_recipe))
        return shopping_list

def generate_shopping_list(recipes: list[tuple[str, str]]) -> list[tuple[float, str, str]]:
    """Return a list of ingredients, (amount, measure, ingredient_name), given a list of recipes.
    """
    new_recipes = recipes.copy()
    shopping_list = []
    for recipe in new_recipes:
        ingredients_bits = recipe[1].split(",")
        for ingredient in ingredients_bits: 
            parsed_ingredient = parse_ingredient(ingredient)
            add_to_shopping_list(parsed_ingredient, shopping_list)

    return shopping_list

def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    """Print the given shopping list in any order you wish. **attempt to print alphabetical

    >>> display_ingredients([(1.0, 'large', 'banana'), (0.5, 'cup', 'ice'),])
        | 1.0 | large | banana |
        | 0.5 | cup   | ice    |
    >>> display_ingredients([(1.0, 'large', 'banana'),
            (2.0, 'tbsp', 'peanut butter'),
            (2.0, 'pitted', 'dates'),
            (1.0, 'tbsp', 'cacao powder'),
            (240.0, 'ml', 'almond milk'),
            (0.5, 'cup', 'ice'),
            (1.0, 'tbsp', 'cocao nibs'),
            (1.0, 'tbsp', 'flax seed')])
        |   1.0 | large  | banana         |
        |   2.0 | tbsp   | peanut butter  |
        |   2.0 | pitted | dates          |
        |   1.0 | tbsp   | cacao powder   |
        | 240.0 | ml     | almond milk    |
        |   0.5 | cup    | ice            |
        |   1.0 | tbsp   | cocao nibs     |
        |   1.0 | tbsp   | flax seed      |
        Here is the output again with visile spaces.
        |␣␣␣1.0␣|␣␣large␣␣|␣banana␣␣␣␣␣␣␣␣␣|
        |␣␣␣2.0␣|␣␣tbsp␣␣␣|␣peanut␣butter␣␣|
        |␣␣␣2.0␣|␣pitted␣␣|␣dates␣␣␣␣␣␣␣␣␣␣|
        |␣␣␣1.0␣|␣␣tbsp␣␣␣|␣cacao␣powder␣␣␣|
        |␣240.0␣|␣␣␣ml␣␣␣␣|␣almond␣milk␣␣␣␣|
        |␣␣␣0.5␣|␣␣␣cup␣␣␣|␣ice␣␣␣␣␣␣␣␣␣␣␣␣|
        |␣␣␣1.0␣|␣␣tbsp␣␣␣|␣cocao␣nibs␣␣␣␣␣|
        |␣␣␣1.0␣|␣␣tbsp␣␣␣|␣flax␣seed␣␣␣␣␣␣|
    """
    """
    1. loop through shopping list, and find biggest amount, measurement, and ingredient
    2. left, right, center allign each bit and print with '|'
    """
    #NOTE need max length of amonut, measurement, ingredient in order to line everything up 
    measure_len = 0
    amount_len = 0
    ingredient_len = 0
    for item in shopping_list:
        for pos, char in enumerate(item):
            if pos == 0 and len(str(char)) > amount_len:
                amount_len = len(str(char))
            elif pos == 1 and len(char) > measure_len:
                measure_len = len(char)
            elif pos == 2 and len(char) > ingredient_len:
                ingredient_len = len(char)

    display_list = list()
    for item in shopping_list:
        for char in item:
            display_list.append(char)
        display_row = [str(display_list[0]).rjust(amount_len, " "), display_list[1].center(measure_len, " "), display_list[2].ljust(ingredient_len, " ")]
        print("|", display_row[0], "|", display_row[1], "|", display_row[2], "|")
        display_list.clear()

def sanitise_comand(comand: str) -> str:
    """return a standardized command to all lowercase and no leading or trailing white spaces, removing 
       any numbers from the string. recipes can only contain lower case letters 
    """
    stripped_comand = comand.strip()
    comand_list = list()
    final_comand = ""


    if 'rm -i' in stripped_comand.lower():  
        for char in stripped_comand:
            if char.isupper():
                comand_list.append(char.lower())
            elif char.islower() or ord(char) == (32 or 45) or char.isnumeric():
                comand_list.append(char)
    else:
        for char in stripped_comand:
            if char.isupper():
                comand_list.append(char.lower())
            elif char.islower() or char.isspace():
                comand_list.append(char) 
    
    for indx in range(len(comand_list)):
        final_comand += comand_list[indx]

    return final_comand.strip()


def main(): 
    """ for commant prompt, will take in a command and call the nessesary function for that command 
        and execute it.
    """
    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE, 
        BROWNIE, 
        SEITAN, 
        CINNAMON_ROLLS, 
        PEANUT_BUTTER, 
        MUNG_BEAN_OMELETTE
    ]

    while True: 
        user_comand = input('Please enter a command: ')
        comand = sanitise_comand(user_comand)
        if comand == 'h': #Help 
            print(HELP_TEXT)
        elif comand == 'q': #Quit
            break
        elif comand == 'g':
#NOTE comand g is the same as ls -s
            pass
        elif comand == 'mkrec': #make recipe / create recipe
            recipe_collection.append(create_recipe)
        elif 'add' in comand:
#NOTE add {recipe}: adds a recipe to the collection.
            # add_recipe(new_recipe='{new recipe}', recipe_collection)
            pass
        elif '-i' not in comand:
#NOTE removes ingredient from shopping list
#NOTE rm -i {ingredient_name} {amount}: removes ingredient from shopping list.
            remove_from_shopping_list()
            pass
        elif 'rm' in comand:
# rm {recipe}: removes a recipe from the collection.
            recipe_collection.pop()#NOTE put something here
            pass
        elif comand == 'ls': #list all recipes in shopping cart
            generate_shopping_list(recipe_collection)
        elif comand == 'ls -a': #List all available recipes in cook book
            print(recipe_collection)
        elif comand == 'ls -s':
            pass
#NOTE havent finished display ingredients yet
#NOTE ls -s: display shopping list.


"""

"""

if __name__ == "__main__":
    main()