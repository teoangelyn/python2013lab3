# decipher.py
from collections import Counter
import itertools

infile = open("MYSTERY.IN", 'r')
outfile = open("RESULT.TXT", 'w')
lines = infile.readlines()
mystery = ''
mystery_list = []
common_list = ['and', 'to', 'the', 'of', 'is', 'on', 'a', 'are', 'our', 'will', 'we', 'We', 'for', 'in', 'as']

for line in lines:
    for a in line:
        ascii_no = ord(a)
        new_ascii_no = ascii_no - 5
        new_alpha = chr(new_ascii_no)
        mystery = mystery + new_alpha
##        print(new_alpha, end='')

##print(mystery)

##print(mystery_list)

# compile words into a list
# words are between 2 spaces
mystery_list = mystery.split(' ')
##print(mystery_list)

# NOTE TO SELF: d must come before e else only the first occurrence will be removed
for d in common_list:
    for e in mystery_list:
        if d == e:
            mystery_list.remove(e)
            

most_common = Counter(mystery_list).most_common(3))
outfile.write(most_common)



    
