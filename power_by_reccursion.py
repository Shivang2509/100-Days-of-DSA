# Problem: Given integers a and b, compute a^b using recursion without using pow() function.

# Input:
# - Two space-separated integers a and b

# Output:
# - Print a raised to power b

# Example:
# Input:
# 2 5

# Output:
# 32

# Explanation: 2^5 = 2 * 2 * 2 * 2 * 2 = 32

def power(a,b):

    if b==0:
        return 1

    return a*power(a, b-1) 

a= int(input("enter the number: "))
b= int(input("enter the power: "))

print (power(a,b))



