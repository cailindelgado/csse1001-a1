from a1 import parse_ingredient, get_recipe_name

def test_get_recipe_name():
    pass

def test_parse_ingredients():
    raw_ingredient_detail = "0.75 cup water"
    output = parse_ingredient(raw_ingredient_detail)
    print(output)
    assert output ==(0.75, "cups", "water") 