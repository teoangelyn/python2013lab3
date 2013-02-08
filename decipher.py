# decipher.py
# decipher.py
from collections import Counter

try: 
    infile = open("MYSTERY.IN", 'r')
    lines = infile.readlines()
    mystery = ''
    mystery_list = []
    common_list = ['and', 'to', 'the', 'can', 'of', 'is', 'on', 'a', 'are', 'our', 'will', 'we', 'We', 'for', 'in', 'as']
    for line in lines:
        for a in line:
            ascii_no = ord(a)
            new_ascii_no = ascii_no - 5
            new_alpha = chr(new_ascii_no)
            mystery = mystery + new_alpha
##        print(new_alpha, end='')


except IOError:
    print("Cannot read from MYSTERY.IN")

try:
    outfile = open("RESULTS.TXT", 'w')
   #  compile words into a list
    mystery_list = mystery.split(' ')

    # NOTE TO SELF: d must come before e else only the first occurrence will be removed
    for d in common_list:
        for e in mystery_list:
            if d == e:
                mystery_list.remove(e)
                

    top_3 = Counter(mystery_list).most_common(3)
    outfile.write('hey')
    for n in top_3:
##        outfile.write(n[0], end=' ')
        print(n[0], end=' ')

except IOError:
    print("Cannot write to RESULTS.OUT")


most_common = Counter(mystery_list).most_common(3))
outfile.write(most_common)
