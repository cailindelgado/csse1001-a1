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