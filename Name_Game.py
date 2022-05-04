#Author: Binod Maharjan
#Program Name: Name Game
#Date: 18/04/2022 
#Version: 1.0.2
#Version date: 04/05/2022

from wsgiref.validate import InputWrapper
import random

print("\nThis is a small game, I used to play when I was a kid.")
input("\nPress Enter to begin the game: ")
print("\n--------------------------------------------")
print('Choose and remember one of the food from the list below:')
rawListMain = ['Apple','Burger','Walnut','Banana','Pizza','Blueberry','Grapes','MoMo','Almond','Papaya','Cake','Pistachio','Orange','Sizzler','Dates']

# the loop below is to print the 15 items of main list in 3 columns and 5 rows
i = 0
while i<15:
    print(rawListMain[i]+'\t'+rawListMain[(i+1)]+'\t'+rawListMain[(i+2)])
    i+=3
input("\nPress Enter when you are done:")

#Make a random list of above the rawListMain.
ListMain = []
i = 1
while i<=rawListMain.__len__():
    r_selected = random.choice(rawListMain)
    ListMain.append(r_selected)
    rawListMain.remove(r_selected)

#There are 4 sub lists made from main list to display them randomly. 
#These sub lists are named as 1, 2, 4 and 8.
choiceList = [1,2,4,8]  
selected = random.choice(choiceList) #Randomly selected 1st one item from above choiceList
choiceList.remove(selected) #Need to remove selected item from the choiceList

ansIndex = 0 #To store the answer of user

#defining the function to display the selected sub list made from main list and returning new answer index
def printSelectedList(selected_choiceList,currAnsIndex):
    print("\n--------------------------------------------")
    print('Is the food item you have remembered listed below:')     
    #printing the selected list
    startingIndex = selected_choiceList-1
    i = 0
    while i<8:
        j = 0
        while j<selected_choiceList:
            print(ListMain[startingIndex])
            startingIndex += 1
            j += 1
            i += 1
        startingIndex+=selected_choiceList
    print() #to print empty line

    #tracking answer from the user    
    while True:
        ans = input('Press \'Y\' for Yes and \'N\' for No: ')
        if ans == 'y' or ans == 'Y':
            newAnsIndex = selected_choiceList + currAnsIndex
            break
        elif ans == 'n' or ans == 'N':
            newAnsIndex = currAnsIndex
            break
        else:
            print('You have not pressed correct key. Please try again.')
    print("--------------------------------------------")
    return newAnsIndex

#running the function(1st time) to print the selected list and get new answer index
ansIndex = printSelectedList(selected,ansIndex)

#selecting 2nd item from the choiceList
selected = random.choice(choiceList) #Randomly selected 2nd time from the choiceList
choiceList.remove(selected) #Need to remove selected item from the choiceList
#running the function(2nd time) to print the selected list and get new answer index
ansIndex = printSelectedList(selected,ansIndex)

#selecting 3rd item from the choiceList
selected = random.choice(choiceList) #Randomly selected 3rd time from the choiceList
choiceList.remove(selected) #Need to remove selected item from the choiceList
#running the function(3rd time) to print the selected list and get new answer index
ansIndex = printSelectedList(selected,ansIndex)

#selecting last item from the choiceList
selected = choiceList[0]
#running the function(4th time) to print the selected list and get new answer index
ansIndex = printSelectedList(selected,ansIndex)

print("--------------------------------------------")
print('The food item you have remembered is '+ ListMain[ansIndex-1]+'.')
print("--------------------------------------------")
input('Press Enter to exit the game: ')

#multiplication table printing
print('\n\nThis program is going to print the Multiplication Table.')
while True:
    try:
        m = int(input("Enter which multiplication table you want to print: "))
    except:
        print('Invalid number input! Please enter only whole numbers.')
    else:
        break
while True:
    try:
        x = int(input("Enter how long the multiplication table you want to go: "))
    except:
        print('Invalid number input! Please enter valid whole number.')
    else:
        break
for i in range(x+1):
    print(m,"x", i,"=",i*m)
input('Press Enter to exit: ')