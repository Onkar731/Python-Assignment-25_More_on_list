"""
Write a python script to create a list of first N terms of a Fibonacci series
"""

# taking input from the user
N = int(input("Enter a number : "))

# creating a list with initial values 0 and 1
l1 = [0, 1]

# defining i for iteration
i = 1

while i <= N :
    l1.append(l1[i-1] + l1[i])
    i += 1

# printing fibonacci terms list
print(l1)