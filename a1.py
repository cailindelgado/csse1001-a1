"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

def num_hours() -> float:
    return 16.42477796077

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
        recipe_bits = recipe[1].split(",")
        for item in range(len(recipe_bits)):
            ingredient_details = parse_ingredient(recipe_bits[item])
            if ingredient == ingredient_details[2]:
                return ingredient_details[0], ingredient_details[1]

def add_to_shopping_list(ingredient_details: tuple[float, str, str], shopping_list: list[tuple[float, str, str] | None]) -> None:
    """Add an ingredient to the shopping list which could either be empty or contain tuples of ingredient details. If the 
       ingredient being added already exists within the list then the amount should be combines. If the ingredient doesn't exist
       then it can be added without any calculations.

       It is assumed that the measure is consistent for all ingredients of the same name. In addition, ingredient_details contains 
       all the information about the ingredient being added to the shopping list. Also, the order doesn't matter. 
    """

    if shopping_list == []:
        shopping_list.append(ingredient_details)
        return

    index = get_index(ingredient_details, shopping_list)
    if index == -1:
        shopping_list.append(ingredient_details)
        return 

    new_ingredient = (shopping_list[index][0] + ingredient_details[0], ingredient_details[1], ingredient_details[2])
    shopping_list[index] = new_ingredient
    return

def get_index(ingredient_details: tuple[float, str, str], shopping_list: list[tuple[float, str, str] | None]) -> int:
    index = -1
    for pos, ingredient in enumerate(shopping_list):
        if ingredient_details[2] == ingredient[2]:  # name matches
            index = pos
            break
    return index

def remove_from_shopping_list(ingredient_name: str, amount: float, shopping_list: list) -> None:
    """Remove a certain amount of an ingredient, with the given ingredient_name, from the shopping list. If the ingredient exists in the shopping_list
       then the amount given as the parameter of this function should be subtracted from the amount that exists in the shopping_list. The ingredient should 
       be removed from the shopping list altogether if the amount goes below 0.
    """
    #NOTE doesnt say i have to remove the item if its amount hits 0
    shopping_list_copy = shopping_list.copy()
    if shopping_list == []:
        return None
    
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
    temp_shopping_list = []
    for recipe in new_recipes:
        ingredients_bits = recipe[1].split(",")
        for ingredient in ingredients_bits: 
            parsed_ingredient = parse_ingredient(ingredient)
            add_to_shopping_list(parsed_ingredient, temp_shopping_list)
    return temp_shopping_list

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
                measure_len = len(char) #+ 2
            elif pos == 2 and len(char) > ingredient_len:
                ingredient_len = len(char) # + 1

    display_list = list()
    for item in shopping_list:
        for bit in item:
            display_list.append(bit)
        
        center_column_space = measure_len + 3 - len(display_list[1])
        left_side = center_column_space // 2
        right_side = center_column_space - left_side
        
        spaces_on_left = left_side * " "
        spaces_on_right = right_side * " "

        display_row = [str(display_list[0]).rjust(amount_len, " "), display_list[1], display_list[2].ljust(ingredient_len + 1, " ")]
        print(f"| {display_row[0]} |{spaces_on_left}{display_row[1]}{spaces_on_right}| {display_row[2]} |")
        display_list.clear()


    #     display_list = list()
    # for item in shopping_list:
    #     for bit in item:
    #         display_list.append(bit)
    #     display_row = [str(display_list[0]).rjust(amount_len, " "), display_list[1].center(measure_len, " "), display_list[2].ljust(ingredient_len, " ")]
    #     print("|", display_row[0], "|", display_row[1], "|", display_row[2], "|")
    #     display_list.clear()

def sanitise_command(command: str) -> str:
    """return a standardized command to all lowercase and no leading or trailing white spaces, removing 
       any numbers from the string. recipes can only contain lower case letters 
    """
    stripped_command = command.strip()
    command_list = list()
    final_command = ""

    if 'rm -i' in stripped_command.lower():  
        for char in stripped_command:
            if char.isupper():
                command_list.append(char.lower())
            elif char.islower() or ord(char) == (32 or 45) or char.isnumeric():
                command_list.append(char)

    for char in stripped_command:
        if char.isupper():
            command_list.append(char.lower())
        elif char.islower() or char.isspace() or ord(char) == 45:
            command_list.append(char) 

    for indx in range(len(command_list)):
        final_command += command_list[indx]

    return final_command.strip()

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

    meal_plan = []

    shopping_list = []

    while True: 
        user_command = input('Please enter a command: ')
        command = sanitise_command(user_command)
        if command == 'h': #Help 
            print(HELP_TEXT)
        elif command.startswith('mkrec'):   #make recipe / create recipe and adds it to collection
            new_recipe = create_recipe()
            recipe_collection.append(new_recipe)
        elif command.startswith('add'):     #add {recipe}: to the recipe collection, adds recipe from recipe collection
            #add an if statement for if recipe cant be found in recipe collection ask user to add a recipe
            if find_recipe(command[4:], recipe_collection) == None:
                print('I suggest making a recipe first')
            
            add_recipe(find_recipe(command[4:], recipe_collection), meal_plan)
              
        elif command.startswith('rm'):
            command_bits = command.split(" ")
            if command_bits[1] == "-i":     # remove ingredient -> rm -i command
                quantity = command_bits[len(command_bits - 1)]
                ingredient_name = "".join(command_bits[3:-1])
                remove_from_shopping_list(ingredient_name, quantity, meal_plan)
            else:                           # rm {recipe}: removes a recipe from the collection.
                recipe_name = command[2:]
                recipe = find_recipe(recipe_name, meal_plan)
                indx = meal_plan.index(recipe)
                recipe_collection.pop(indx)
                #couldnt i just do recipe_collection.pop(recipe_collection.index(recipe))
                #couldnt i just do recipe_collection.pop(recipe_collection.index(find_recipe(recipe_name, recipe_collection)))
        elif command[:5] == 'ls -a': #ls -a list all available recipes
            for indx in range(len(recipe_collection)):
                print(recipe_collection[indx][0])
        elif command[:5] == 'ls -s': #ls -s display shopping list
            display_ingredients(shopping_list)
        elif command[:2] == 'ls':     #ls list all recipes in meal plan 
            if meal_plan == []:
                print('No recipe in meal plan yet.')
            else:
                print(meal_plan)
        elif command == 'g':           #generates shopping list for display_ingredients to display from
            shopping_list.clear()          
            shopping_list += generate_shopping_list(meal_plan)
            display_ingredients(shopping_list)
        elif command == 'q':                #Quit
            break
        else:
            print('if you enter H or h you will get help')

#NOTE List of recipes, cookbook, and recipe collection are the same thing.
#NOTE Shopping list and cart are the same thing pretty much, but you'd find that the rm and rm -i commands refer to different lists. Just keep that in mind considering how many lists you want to make. 

if __name__ == "__main__":
    main()