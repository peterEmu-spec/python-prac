
"""
1.Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

"""
squares = [i**2 for i in range(1,30+1)]

fv = squares[:5]
lv = squares[-5:]

print(fv)
print(lv)

"""
2.Write a Python program to calculate the difference between the two lists.

"""
def subtract ():
#summation of first five 
    num=0
    for i in fv:
        num += i
#summation of last five
    num2 =0
    for i in lv:
        num2 += i
    
    return num2-num

print(subtract())
    





