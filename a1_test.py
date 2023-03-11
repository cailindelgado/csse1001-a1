from a1 import parse_ingredients

def test_parse_ingredients():
    raw_ingredient_detail = "0.75 cup water"
    output = parse_ingredients(raw_ingredient_detail)
    print(output)