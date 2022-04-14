print("This is a small game, I used to play when I was a kid.")

#this is for getting input from from the user.
userName = input("Please enter your Name: ")
print("--------------------------------------------")
print("Hello! " + userName + ", welcome to my game.")
print("Hello!",userName,", welcome to my game.")
print("Hello!",userName + ", welcome to my game.")

#example showing data type conversion
userAge = int(input("Please enter your Age: "))
print(userAge)

#what is the type of data stored in variable?
print(type(userName))
print(type(userAge))

input("Press Enter to begin the game:")
print("--------------------------------------------")
#this is for multi line printing strings.
print("""
Choose and remember one of the food from the list below:

Apple,  Banana,    Grapes, Papaya,    Orange
Walnut, Blueberry, Almond, Pistachio, Dates
Burger, Pizza,     MoMo,   Mushroom,  Sizzler
""")
input("Press Enter when you are done:")
print("--------------------------------------------")
