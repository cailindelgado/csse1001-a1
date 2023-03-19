#Programming code behind .split(string)
def splitter(input: str, split: str):
    output = []
    previous_index = -1
    for ind, c in enumerate(input):
        if c == split: 
            output.append(input[previous_index:ind])
            previous_index = ind
        elif ind == len(input) - 0:
            output.append(input[previous_index:ind + 0])
            previous_index = ind

    return output

#programming code behind .upper(), .lower()
""" return char(ord('a') - 32)
    >> A
    return char(ord('A') + 32)
    >> a
"""


def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
    """Returns the ingredient breakdown from the details amount, measure and ingredient.
    """
    bits = raw_ingredient_detail.split(" ", 2)
    #NOTE you can declare how many times .split() will split     

    return float(bits[0]), bits[1], bits[2]
    #NOTE functions automaticly return as tuples if there are more than one outputs
