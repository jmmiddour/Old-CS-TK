# Time Complexity (TC) = O(n) - Polynomial
# Space Complexity (SC) = O(1) - Constant
def linear_search(arr, target):
    for i in range(len(arr)):  # TC = O(n)
        if arr[i] == target:   # TC = O(1)
            return i

    return -1   # not found

# Another way to do it
# def linear_search(arr, target):
#     for index, element in enumerate(arr):
#         if element == target:
#             return index
#
#     # Or can do the above for loop as an if statement
#     #   but will still be the same in time complexity.
#     # The above for loop might even be slightly faster.
#
#     if target in arr:
#         return arr.index(target)
#
#     return -1  # not found


# Write an iterative implementation of Binary Search
# Time Complexity (TC) = O(log n) - Logarithmic
# Space Complexity (SC) = O(1) - Constant
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:              # TC = O(log n)
        middle = (low + high) // 2  # TC = O(1), SC = O(1)
        guess = arr[middle]         # TC = O(1), SC = O(1)

        if guess == target:         # TC = O(1)
            return middle           # TC = O(1)

        elif guess > target:        # TC = O(1)
            high = middle - 1       # TC = O(1), SC = O(1)

        else:                       # TC = O(1)
            low = middle + 1        # TC = O(1), SC = O(1)

    return -1  # not found


# Another way to do it
# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         middle = (left + right) // 2
#
#         if arr[middle] == target:
#             return middle
#
#         elif arr[middle] > target:
#             right = middle - 1
#
#         else:
#             left = middle - 1
#
#     return -1  # not found