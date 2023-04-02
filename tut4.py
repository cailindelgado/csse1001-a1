# file = open("week06_bad_config1.txt", 'w')
# content = """
# [user]
# name=Eric Idle
# this line is bad
# mobile=0412345678
# [notifications]
# email=yes
# sms=no
# """

# file.write(content)
# file.close()

# file_read = open('week06_bad_config1.txt')

# print(file_read) 
# for line in file_read.read().split('\n'):
#     print(line)
# file_read.clost()

def find_functions(filename: str) -> str: 
    fin = open(filename, 'r')
    fout = open('functions.txt', 'w')
    for line in fin: 
        if line.startswith('def'):
            fout.write(line.rstrip() + '\n')

    fin.close()
    fout.close()


def function_bits(filename: str): 
    fin = open(filename, 'r')
    return_args = []
    for line, info in  enumerate(fin, 1): 
        info =info[4:]
        name, _, line = line.partition("(")
        args = line.partition(")")[0]
        for arg in args.split(','):
            return_args.append(arg)

    fin.close()
    return (return_args)
#.partition() is a string method that always return a tuple with a length of 3., look at w3 schools for more information.

# print(function_bits('foo.txt'))



