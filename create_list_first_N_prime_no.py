"""
Write a python script to create a list of first N prime numbers
"""

# taking input from the user
N = int(input("Enter a number : "))

# creating an empty list
prime_list = []

# appending prime numbers in list
j = 2

while N != 0 :
    i = 2
    while i*i <= j :
        if j % i == 0 :
            break;
        i += 1
    else :
        prime_list.append(j)
        N -= 1
    j += 1

# printing prime list      
print(prime_list)