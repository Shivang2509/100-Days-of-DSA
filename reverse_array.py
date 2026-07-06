""" Problem: Given an array of n integers, reverse the array in-place using two-pointer approach.

Input:
- First line: integer n
- Second line: n space-separated integers

Output:
- Print the reversed array, space-separated

Example:
Input:
5
1 2 3 4 5

Output:
5 4 3 2 1

Explanation: Swap pairs from both ends: (1,5), (2,4), middle 3 stays """




""" CODE """

n= int(input("Enter the no. of array: "))
arr = list(map(int, input("Enter the array with space: ").split()))

left=0
right=n-1

while left<right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("The reversed array is: ", *arr)
