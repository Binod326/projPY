#Author: Binod Maharjan
#Program Name: Playing with the list
#Version: 0.0.1
#Date: 18/04/2022 
import random

rawListMain = ['Apple','Burger','Walnut','Banana','Pizza','Blueberry','Grapes','MoMo','Almond','Papaya','Cake','Pistachio','Orange','Sizzler','Dates']
print(rawListMain)

#Make a random list of above ListMain.
ListMain = []
i = 1
while i<=rawListMain.__len__():
    r_selected = random.choice(rawListMain)
    ListMain.append(r_selected)
    rawListMain.remove(r_selected)
    print(r_selected)
    print(ListMain)
    print(rawListMain.__len__())
    print()