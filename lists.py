
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
    
    #question 3
sample_list = ['p', 'q']
n = 5

result = [item + str(i) for i in range(1, n+1) for item in sample_list]

print(result)

#question 4
colors = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result = [{'color_name': c, 'color_code': d} for c, d in zip(colors, codes)]

print(result)
 
#question 5
nums = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

result = [x for x in nums if x != 0] + [0] * nums.count(0)

print("Original:", nums)
print("After  zeros:", result)

#question 6
nums = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]

rounded = [round(x) for x in nums]
print("Minimum value:", min(rounded))
print("Maximum value:", max(rounded))

multiplied = sorted(set([x * 5 for x in rounded]))

print("Result:")
print(*multiplied)

# question 7
lst = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]

count = sum(1 for item in lst if isinstance(item, list))

print("The number of lists:", count)






