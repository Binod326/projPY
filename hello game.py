from wsgiref.validate import InputWrapper
import random

print("This is a small game, I used to play when I was a kid.")
'''
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
'''

input("Press Enter to begin the game: ")
print('Choose and remember one of the food from the list below:')
ListMain = ['Apple','Burger','Walnut','Banana','Pizza','Blueberry','Grapes','MoMo','Almond','Papaya','Cake','Pistachio','Orange','Sizzler','Dates']
i = 0
while i<15:
    print(ListMain[i]+'\t'+ListMain[(i+1)]+'\t'+ListMain[(i+2)])
    i+=3
input("Press Enter when you are done:")

ansIndex = 0
choiceList = [1,2,4,8]
selected = random.choice(choiceList)
print(selected)
choiceList.remove(selected)
print(choiceList)

def printSelectedList():
    #print the selected list
    startingIndex = selected-1
    i = 0
    while i<8:
        j = 0
        while j<selected:
            print(ListMain[startingIndex])
            startingIndex += 1
            j += 1
            i += 1
        startingIndex+=selected
    #tracking answer from the user    
    ans = input('Press \'Y\' for Yes and \'N\' for No: ')
    if ans == 'y' or ans == 'Y':
        ansIndex = selected + int(ansIndex)
    print('Answer index is ' + str(ansIndex))
    print("--------------------------------------------")

print('Is the food item you have remembered listed below:')
printSelectedList()

selected = random.choice(choiceList)
print(selected)
choiceList.remove(selected)
print(choiceList)
print('Is the food item you have remembered listed below:')
printSelectedList()

selected = random.choice(choiceList)
print(selected)
choiceList.remove(selected)
print(choiceList)
print('Is the food item you have remembered listed below:')
printSelectedList()

selected = choiceList[0]
print(selected)
print('Is the food item you have remembered listed below:')
printSelectedList()

print("--------------------------------------------")
print('The food item you have remembered is '+ ListMain[ansIndex-1])
print("--------------------------------------------")
