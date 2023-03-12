"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

def num_hours() -> float:
    return 7.28

# Fill these in with your details
__author__ = "Cailin H Delgado"
__email__ = "c.delgado@uqconnect.edu.au"
__date__ = "03/03/2023"

from constants import *

# Write your functions here

def get_recipe_name(recipe: tuple([str, str])) -> str:
    """Returns the name of the recipe.
        get_recipe_name('chocco banana milkshake', '1.3 bananas')
    >> 'chocco banana milkshake'
    """
    return recipe[0]

def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
    """Returns the ingredient breakdown from the details amount, measure and ingredient.
    """
    details_of_ingredient = raw_ingredient_detail.split(" ")
    return (float(details_of_ingredient[0]), details_of_ingredient[1], details_of_ingredient[2])
      
def create_recipe() -> tuple[str, str]:
    """Returns the recipe in the tuple[str, str] format after a series of prompting. 
       The recipe name is prompted first followed by continuous ingredient prompting
       until an empty string is returned. 
    """
    recipe_name = input("please enter the recipe name: ")
    recipe_list = list()
    recipe_list.append(recipe_name)
    recipe_ingredients = ""
    recipe_final_ingredients = ""
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
    print(tuple(ingredient_breakdown))
    return tuple(ingredient_breakdown)

def add_recipe(new_recipe: tuple[str, str], recipes: list[tuple[str, str]]):
    """Add a given recipe, new_recipe, into the list of recipes.
       Hint: this function doesn't return anything  """
    #add the inputted recipe to the list of tuples recipe:
    recipes += new_recipe
#NOTE why arent brackets appearing around the new insert

def find_recipe(recipe_name: str, recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
    """This function find and returns a recipe with a given recipe_name if it cannot be found returns None 
    """
    check_for_similarity_counter = 0  
    for char in recipes:
        if recipe_name not in char:
            check_for_similarity_counter += 1 
    
    if check_for_similarity_counter == len(recipes):
        return None

    for pos, char in enumerate(recipes):
        if recipe_name in char: 
           return recipes[pos]

def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    """remove a recipe from the list of recipes given the name of a recipe. If the recipe 
       name doesn't match any of the recipes withing the list of recipes then nothing happens
    """
    recipes_list = list(recipes) 
    for pos, tup in enumerate(recipes_list):
        if name not in tup:
            return None
        else:
            recipes_list.pop(pos)
    print(tuple(recipes_list))
#NOTE come back to this later

def get_ingredient_amount(ingredient: str, recipe: tuple[str, str]) -> tuple[float, str] | None:
    """Return the amount and measure of a certain ingredient as a tuple[float, str] given an ingredient name 
       as a str and a recipe. If the ingredient doesnt exist then nothing happens
    """
    ingredient_list = list(parse_ingredient(recipe[1]))
    print(ingredient_list)
    

        


def add_to_shopping_list(ingredient_details: tuple[float, str, str], shopping_list: list[tuple[float, str, str] | None]) -> None:
    """Add an ingredient to the shopping list which could either be empty or contain tuples of ingredient details. 
       If the ingredient being added already exists within the list then the amount should be combines. If the ingredient doesn't exist
       then it can be added without any calculations.

       It is assumes that the measure is consistent for all ingredients of the same name. In addition, ingredient_details contains all the
       information about the ingredient being added to the shopping list. Also, the order doesn't matter. 
    """

def remove_from_shopping_list(ingredient_name: str, amount: float, shopping_list: list) -> None:
    """Remove a certain amount of an ingredient, with the given ingredient_name, from the shopping list. If the ingredient exists in the shopping_list
       then the amount given as the parameter of this function should be subtracted from the amount that exists in the shopping_list. The ingredient should 
       be removed from the shopping list altogether if the amount goes below 0.
    """

def generate_shopping_list(recipes: list[tuple[str, str]]) -> list[tuple[float, str, str]]:
    """Return a list of ingredients, (amount, measure, ingredient_name), given a list of recipes.
    """

def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    """Print the given shopping list in any order you wish. **attempt to print alphabetical
    """

def sanitise_command(commnd: str) -> str:
    """return a standardized command to all lowercase and no leading or trailing white spaces, removing any numres from the string.
       recipes can only contain lower case letters 
    """

def main_func() -> None:
#    command = input('Please enter a command: ')
#    while command != 'quit':
#        if command == 'h' or 'H':
#            print(HELP_TEXT)
#            break
    pass


def main():
    """ Write your docstring """
    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE, 
        BROWNIE, 
        SEITAN, 
        CINNAMON_ROLLS, 
        PEANUT_BUTTER, 
        MUNG_BEAN_OMELETTE
    ]

if __name__ == "__main__":
    main()