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


def sanitise_comand(comand: str) -> str:
    """return a standardized command to all lowercase and no leading or trailing white spaces, removing 
       any numbers from the string. recipes can only contain lower case letters 
    """
    stripped_comand = comand.strip()
    comand_list = list()
    final_comand = ""

    if 'rm -i' in stripped_comand.lower():  
        for pos, char in enumerate(stripped_comand):
            if ord(char) >= 65 and ord(char) <= 90:
                comand_list.append(chr (ord(char) + 32))
            elif (ord(char) >= 97 and ord(char) <= 122) or ord(char) == (32 or 45) or (ord(char) >= 48 and ord(char) <= 57):
                comand_list.append(char)
            if ord(char) == 45 and stripped_comand[pos + 1] == ord(char): 
                pass
    else:
        for char in stripped_comand:
            if ord(char) >= 65 and ord(char) <= 90:
                comand_list.append(chr (ord(char) + 32))
            elif (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 32:
                comand_list.append(char) 
    
    for indx in range(len(comand_list)):
        final_comand += comand_list[indx]

    return final_comand.strip()
