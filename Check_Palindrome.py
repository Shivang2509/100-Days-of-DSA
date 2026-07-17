# Problem: Read a string and check if it is a palindrome using two-pointer comparison.

# Input:
# - Single line: string s

# Output:
# - Print YES if palindrome, otherwise NO

# Example:
# Input:
# level

# Output:
# YES

# Explanation: String reads same forwards and backwards

#CODE
s=list(input("Enter the string: "))

i=0
j=len(s)-1

while i<j:
    if s[i]==s[j]:
        i+=1
        j-=1
        print("YES")
        break
    
    else:
        print('NO')
        break