from wsgiref.validate import InputWrapper

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

Apple\t\tBanana\t\tGrapes\t\tPapaya\t\tOrange
Walnut\t\tBlueberry\tAlmond\t\tPistachio\tDates
Burger\t\tPizza\t\tMoMo\t\tMushroom\tSizzler
""")
input("Press Enter when you are done:")
print("--------------------------------------------")
