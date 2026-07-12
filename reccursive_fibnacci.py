# Problem: Write a recursive function fib(n) to compute the n-th Fibonacci number where fib(0)=0 and fib(1)=1.

# Input:
# - Single integer n

# Output:
# - Print the n-th Fibonacci number

# Example:
# Input:
# 6

# Output:
# 8

# Explanation: Sequence: 0,1,1,2,3,5,8 at positions 0,1,2,3,4,5,6



# CODE

n= int(input("enter the nth term of fibnacci series: "))

if n==0:
    print(0)

elif n==1:
    print(1)
    
else:
    i=0
    j=1

    for a in range (2,n+1):
        k=i+j
        i=j
        j=k

    print(k)



