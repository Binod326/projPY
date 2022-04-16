#below is the example of multi line comment
"""
escape character '\'
\n for new line
\t for tab
\r for Carriage Return (\r is used to shift the cursor to the begining of the line)
"""
print('That\'s my father\'s car.')
print("The first line.\nThis is the second line.\n\\n is used to enter new line.")
print('abc\rde')

#this is for multi line printing strings.
print("""
Choose and remember one of the food from the list below:

Apple\t\tBanana\t\tGrapes\t\tPapaya\t\tOrange
Walnut\t\tBlueberry\tAlmond\t\tPistachio\tDates
Burger\t\tPizza\t\tMoMo\t\tMushroom\tSizzler
""")
print('''
Hello World!
This is also Multi line.
Good Luck!!!
''')

#Concatenation using '+'
print("Spam"+'eggs')
#Repeat the same string multiple times use '*'
print(4 * 'Notice! ')
print(2*'pa'+'ya')
print('a'+'b'*(2**3))
print(('a'+'b')*(2**3))