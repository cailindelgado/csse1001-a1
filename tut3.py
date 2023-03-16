
#NOTE tutortial on data structures 

def is_dna(dna: str) -> bool:
    #with an input of dna 
    x = len(dna)
    if x % 3 == 0 and ('A' and'T' and 'G' and 'C') in dna:
       return True
    else: 
        return False

# is_dna("AATGAC")
# is_dna("AATGD")


# def reverse_complement(dna: str) -> str:
    dna.replace('A', 'T')
    dna.replace('G', 'C')
    if is_dna(dna) == True:
        print()
    else:
        print('None')

# reverse_complement('AATGAC')
# reverse_complement('GATTACAAA')
# reverse_complement('GAGA')

"""
def reverse_complement(dna: str) -> bool | none:
    if not is_dna(dna):
        return None
    mapping = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    reverse_dna = dna[::-1]
    s = ""
    for char in reverse_dna:
    s += mapping.get(char)
    return s
"""


# def print_codeons(dna: str) -> str:
#     if is_dna(dna) == True:
#         print[0:2:3]
            
#dna[start:end:step]            
# print_codeons('GATTACAAA')
# print_codeons('AATGAC')
# print_codeons("GAGA")

# def generate_codeons(dna: str):
#     if is_dna(dna):
#         codons = []
#         for i in range(0, len(dna), 3):
#             codons.append(dna[i: i + 3])
#     else: 
#         codeons = None
    
#     return codons

# def print_codons(dna: str) -> None:
#     if dna is not None:
#         for codon in dna: 
#             print(codon)