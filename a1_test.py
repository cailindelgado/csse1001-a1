from a1 import get_recipe_name, parse_ingredient, create_recipe, recipe_ingredients

def test_get_recipe_name():
    recipe = ('chocolate peanut butter banana shake', '1 large banana,2 tbsp peanut butter')
    output = get_recipe_name(recipe)
    assert output == 'chocolate peanut butter banana shake'
    # return output


def test_parse_ingredients():
    raw_ingredient_detail = "0.75 cup water"
    output = parse_ingredient(raw_ingredient_detail)
    assert output == (0.75, 'cup', 'water')
    # return output

def test_create_recipe():
    recipe = create_recipe()
    return recipe
###                                                         NOTE: passed

def test_recipe_ingredients():
    recipe = (("peanut butter", '300 g peanuts,0.5 tsp salt,2 tsp oil'))
    output = recipe_ingredients(recipe)
    # assert output == ((300.0, 'g', 'peanuts'), (0.5, 'tsp', 'salt'), (2.0, 'tsp', 'oil'))
    return output
