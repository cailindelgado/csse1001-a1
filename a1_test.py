import io
import pytest
from constants import *
from a1 import get_recipe_name, parse_ingredient, create_recipe, recipe_ingredients, add_recipe, find_recipe, remove_recipe, get_ingredient_amount

def test_get_recipe_name():
    recipe = ('chocolate peanut butter banana shake', '1 large banana,2 tbsp peanut butter')
    output = get_recipe_name(recipe)
    assert output == 'chocolate peanut butter banana shake'
    # return output


def test_parse_ingredients():
    raw_ingredient_detail = "0.75 cup water of life"
    output = parse_ingredient(raw_ingredient_detail)
    assert output == (0.75, 'cup', 'water of life')
    # return output

@pytest.mark.skip()
def test_create_recipe():
    recipe = create_recipe()
    # assert recipe == ('chocolate', '20 ml milk,300 g peanuts,50 g dough')
    """ create_recipe()
    >>> please enter a recipe name: chocolate
    >>> please enter an ingredient: 20 ml milk 
    >>> please enter an ingredient: 300g peanuts 
    >>> please enter an ingredient: 2 tsp oil
    >>> please enter an ingredient:
    ('chocolate', '20 ml milk,300 g peanuts, 2 tsp oil')
    """

def test_recipe_ingredients():
    recipe = ("peanut butter", '300 g peanuts,0.5 tsp salt,2 tsp oil')
    output = recipe_ingredients(recipe)
    assert output == ((300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'))

def test_add_recipe():
    new_recipe = ('peanut butter', '300g peanuts,0.5tsp salt,2 tsp oil')
    recipes  = [CHOCOLATE_PEANUT_BUTTER_SHAKE, BROWNIE, SEITAN, CINNAMON_ROLLS, PEANUT_BUTTER, MUNG_BEAN_OMELETTE]
    output = add_recipe(new_recipe, recipes)
    return output
    """
    >>> recipes = []
    >>> recipe = ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
    >>> add_recipe(recipe, recipes)
    >>> recipes
    [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    >>> add_recipe(recipe, recipes)
    >>> recipes
    [('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil'), ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')]
    """

def test_find_recipe():
    recipe_name = 'peanut butter'
    recipe = [CHOCOLATE_PEANUT_BUTTER_SHAKE, BROWNIE, SEITAN, CINNAMON_ROLLS, PEANUT_BUTTER, MUNG_BEAN_OMELETTE]
    output = find_recipe(recipe_name, recipe)
    return output

def test_remove_recipe():
    name = 'peanut butter'
    recipe = [CHOCOLATE_PEANUT_BUTTER_SHAKE, BROWNIE, SEITAN, CINNAMON_ROLLS, PEANUT_BUTTER, MUNG_BEAN_OMELETTE]
    output = remove_recipe(name, recipe)
    # assert output == [CHOCOLATE_PEANUT_BUTTER_SHAKE, BROWNIE, SEITAN, CINNAMON_ROLLS, MUNG_BEAN_OMELETTE]

def test_get_ingredient_ammount():
    ingredient = 'peanuts' 
    recipe = [PEANUT_BUTTER]
    output = get_ingredient_amount(ingredient, recipe)
    return output
    