# Problem: A secret system stores code names in forward order. To display them in mirror format, you must transform the given code name so that its characters appear in the opposite order.

# Input:
# - Single line: a lowercase string containing only alphabetic characters (no spaces)

# Output:
# - Print the transformed code name after applying the mirror operation

# Example:
# Input:
# hello

# Output:
# olleh

# Explanation: The first character moves to the last position, the second to the second-last, and so on until the entire string is mirrored


#CODE
s=list(input("Enter the string: "))

i=0
j=len(s)-1

while i<j:
    s[i],s[j]=s[j],s[i]
    i+=1
    j-=1

print(s)
