// Problem: Implement linear search to find key k in an array. Count and display the number of comparisons performed.

// Input:
// - First line: integer n (array size)
// - Second line: n space-separated integers
// - Third line: integer k (key to search)

// Output:
// - Line 1: "Found at index i" OR "Not Found"
// Line 2: "Comparisons = c"

// Example:
// Input:
// 5
// 10 20 30 40 50
// 30

// Output:
// Found at index 2
// Comparisons = 3

// Explanation: Compared with 10, 20, 30 (found at index 2 with 3 comparisons)





# Input
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

comparisons = 0

# Linear Search
for i in range(n):
    comparisons += 1
    if arr[i] == k:
        print("Found at index", i)
        print("Comparisons =", comparisons)
        break
else:
    print("Not Found")
    print("Comparisons =", comparisons)