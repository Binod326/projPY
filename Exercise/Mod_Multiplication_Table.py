#Author: Binod Maharjan
#Program Name: Printing multiplication table as long as user want
#Date: 05/05/2022 
#Version: 0.0.1
#Version Date: 05/05/2022

def multiplicationTable(x,y):
    
    table = ''
    for i in range(y+1):
        table += f'{x} x {i} = {x*i}\n'
    return table  