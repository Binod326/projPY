#this file is about the operators and decision making in Python 

###OPERATORS IN PYTHON

#Arithmetic operators
# + - * / %Modulus(Reminder) **Exponent(power) //Truncation or Floor Division(quotient)

print(7+3)
print("Subtraction of 7 - 3 is",7-3)
print(7*3)
print(7/3)
print(7%3)  #Ans: 1 (reminder)
print(7**3)
print(7//3) #Ans: 2 (quotient)

#Comparision operators
# > < == != >= <=
print("7 is greater than 3:",7>3)
print("7 is less than 3:",7<3)
print("7 is equal to 3:",7==3)
print("7 is not equal to 3:",7!=3)
print("7 is greater or equal to 3:",7>=3)
print("7 is less or equal to 3:",7<=3)

#Logial operators
# and --> returns True if both the operands are ture
# or  --> returns True if either of the operands are ture
# not --> returns True if operands is false
x = True
y = False
print('x is',x)
print('y is',y)
print("x and y is", x and y)
print("x or y is", x or y)
print('not x is', not x)
print('not y is', not y)


###DECISION MAKING IN PYTHON

#Conditional statements:
# If statement, If-else statement, If-elif-else statement, Nested If-else statement
age = int(input("Enter you age: "))
if age>=18:
    print("Congratulations, you are eligible to vote")
print('checking if statement')
"""    
else:
    print("Sorry, you are not eligible to vote")
    
                
"""