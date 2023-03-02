#Author: Binod Maharjan
#Program Name: Printing multiplication table as long as user want
#Date: 04/05/2022 
#Version: 0.0.1

# using while loop, for loop and exception handling
'''try:
    m = int(input("Enter which multiplication table you want to print: "))
except ValueError:
    print('Invalid number! Please enter only whole numbers.')
    m = int(input("Enter which multiplication table you want to print: "))
else:
    print('this is else statment.')
finally:
    print('This is finally statement.')'''
import datetime as date
print(date.datetime.now())
print(date.datetime.today())
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