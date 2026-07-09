""" Problem: Given a sorted array of n integers, remove duplicates in-place. Print only unique elements in order.

Input:
- First line: integer n
- Second line: n space-separated integers (sorted array)

Output:
- Print unique elements only, space-separated

Example:
Input:
6
1 1 2 2 3 3

Output:
1 2 3

Explanation: Keep first occurrence of each element: 1, 2, 3 """







""" CODE """

n= int(input("Enter the number of array: "))
arr= list(map(int, input("Enter the array with space: ").split()))

i=0
j=1

while j<n:
    if arr[i] != arr[j]:
        i+=1
        arr[i] = arr[j]
    j+=1


for k in range (i+1,):
    print (arr[k], end=" ")






