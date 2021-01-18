# This might help give a visual of the different sorting methods.
# https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html

# TO-DO: Complete the selection_sort() function below
# 1. Start with current index = 0
# 2. For all indices EXCEPT the last index:
#    - Loop through elements on the right-hand side of the current index
#      and find the smallest element.
#    - Swap the element at current index with the smallest element
#      found in above loop.

# Time complexity (TC) = Quadratic - O(n^2)
# Space Complexity (SC) = Constant - O(1)

def selection_sort(arr):
    # Loop through n-1 elements
    for i in range(0, len(arr) - 1):  # TC = O(n)
        cur_index = i                 # TC = O(1), SC = O(1)
        smallest_index = cur_index    # TC = O(1), SC = O(1)

        # Find the next smallest element
        #   (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):  # TC = O(log n)
            if arr[j] < arr[smallest_index]:  # TC = O(1)
                smallest_index = j            # TC = O(1), SC = O(1)

        # Swap - TC = O(1)
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

# Selection Sort:

# Time Complexity (TC) = (n) * (1 + 1 + log n) * (1 + 1)
#                        n * 2 log n * n
#                        2n * 2 log n
# Final TC             = O(n log n)

# Space Complexity (SC) = 1 + 1 + 1
# Final SC              = O(1)


# TO-DO:  implement the Bubble Sort function below
# 1. Loop through your array
#   - Compare each element to its neighbor
#   - If elements are in the wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop.
#    Else, go back to the element at index 0 and repeat step 1

# Time complexity (TC) = Quadratic - O(n^2)
# Space Complexity (SC) = Constant - O(1)

# Morning Code
def bubble_sort(arr):
    # Iterates through first number
    for i in range(len(arr) - 1):                        # TC = O(n),

        # Iterates over the value to the right of i
        for j in range(len(arr) - 1 - i):                # TC = O(n),

            # If j is > value to the right of j, they swap places
            if arr[j] > arr[j + 1]:                      # TC = O(1), SC - O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # TC = O(1),
#                                                          TC = Polynomial O(n^2)
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''

# Time Complexity (TC) =
# Space Complexity (SC) =


# def counting_sort(arr, maximum=None):
#     output = [0 for i in range(len(arr))]
#
#     count = [0 for i in range(maximum)]
#
#     for i in arr:
#         count[i] += 1
#
#     # for i in range(maximum):
#     #     output[count[arr[i]]]
#
#     for i in range(1, len(arr)):
#         count[i] += count[i -1]
#
#     for i in range(len(arr)):
#         output[count[arr[i] - 1]]
#
#     return arr

# Code from https://www.programiz.com/dsa/counting-sort
def counting_sort(arr):
    size = len(arr)
    output = [0] * size

    # Initialize the count array
    count = [0] * 10

    # Store the count of each element in the count array
    for i in range(0, size):
        count[arr[i]] += 1

    # Store the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in the count array
    #   place the elements in the output array
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    # Copy the sorted elements into the original array
    for i in range(0, size):
        arr[i] = output[i]

    return arr
