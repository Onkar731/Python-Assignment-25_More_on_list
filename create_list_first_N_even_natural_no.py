"""
Write a python script to create a list of first N even natural numbers
"""

# taking input from the user
N = int(input("Enter a number : "))

# creating a list using list comphrension 
l1 = [e*2 for e in range(1, N+1)]

# printing list
print(l1)