"""
Write a python script to create two lists from a given list of numbers in such 
a way that the first list can have only positive numbers and second list can have
only non-positive numbers.
"""

# creating a list of positive and non-positive elements list
l1 = [12, 43, 24, -23, -5, -2, 87, -98, 45, 98, 67, -123, 0, 458, -567]

# creating two list of positive and non-positive elements
positive_list, non_positive_list = list(), list()

for e in l1 :
    if e > 0 :
        positive_list.append(e)
    else :
        non_positive_list.append(e)
        
# printing both the list positive and non-positive
print("Positive Elements List :", positive_list)
print("Non-Positive Element List :", non_positive_list)