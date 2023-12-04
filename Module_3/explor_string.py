name = 'Tamim\'s Iqbal' #escape
name2 = "tamim iqbal"
#multiline string
name3 = """ 
    Tamim
    Iqbal
"""

print(name)
print(name2)
print(name3)

#string sequence of character
for char in name2:
    print(char)

#muteable means change able is a list
#immuteable means can't change the string
# name[0] = 'R'
# print(name)

#check a string a full string 
if 'iqbal' in name2:
    print('Exsits')

print(name[4])
print(name[-2])
print(name[1:7])
print(name[::-1])

print(name.upper()) #all char capital letter
print(name.lower()) # all char small letter
print(name.title()) # first leter a string a capital letter 
print(name.swapcase()) # first leter is small letter and other letter is capital letter
print(name.capitalize()) # for the very first letter is capital letter just
print(name.casefold())
print(name.center(5))
char_count = name.count('a')
print(char_count)