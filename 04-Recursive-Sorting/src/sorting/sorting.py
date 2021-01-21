# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # Getting the sum of the lengths of both arrays to create the merged array
    elements = len(arrA) + len(arrB)

    # Creates a merged array that is a list of 0's,
    #   the length of the combined lengths of arrA and arrB
    # Creating the array at a defined length before is better for
    #   space and time complexity (at least a little bit)
    merged_arr = [0] * elements  # Initializes the "buckets"

    # Create variables to compare the arrays
    index_a = 0
    index_b = 0

    # Iterate through the merged array using range to get the index
    for i in range(len(merged_arr)):
        # If arrA doesn't exist or if index_a has gone beyond the length of arrA
        if index_a > len(arrA) - 1:
            # Set the current spot in merged array to the next value in arrB
            merged_arr[i] = arrB[index_b]
            # Increment index_b by one on each iteration
            index_b += 1

        # If arrB doesn't exist or if index_b has gone beyond the length of arrB
        elif index_b > len(arrB) - 1:
            # Set the current spot in merged array to the next value in arrA
            merged_arr[i] = arrA[index_a]
            # Increment index_a by one on each iteration
            index_a += 1

        else:
            # If the index of arrA is greater than the arrB index
            if arrA[index_a] > arrB[index_b]:
                #
                merged_arr[i] = arrB[index_b]
                # Increment index_a by one on each iteration
                index_b += 1

            else:
                #
                merged_arr[i] = arrA[index_a]
                # Increment index_a by one on each iteration
                index_a += 1

    # Return the merge sorted array
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Need to get the middle point of the array
    middle = len(arr) // 2
    # Keeping track of the middle while grabbing everything before the middle
    left_side = arr[:middle]
    # Keeping track of the middle while grabbing everything from the middle to the end
    right_side = arr[middle:]

    # If the length of the array before the middle is greater than 1
    if len(left_side) > 1:
        # Recurse through the array before the middle,
        #   assign the new left side, using the function above
        left_side = merge_sort(left_side)

    # If the length of the array from middle to the end is greater than 1
    if len(right_side) > 1:
        # Recurse through the array from the middle to the end,
        #   assign the new right side, using the function above
        right_side = merge_sort(right_side)

    # Merge the final left and right sides together
    arr = merge(left_side, right_side)

    # Return the final merge sorted array
    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input

# Morning code taken from https://www.geeksforgeeks.org/in-place-merge-sort/
# Merges two sub-arrays of an array
# First sub-array is from the left (start) to the middle of the array
# Second sub-array is from the middle to the right (end) of the array
# This is the inplace implementation
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1

    # If the direct merge is already sorted
    if arr[mid] <= arr[start2]:
        return

    # Need 2 pointers to maintain the start of both arrays to be merged
    while start <= mid and start2 <= end:

        # If element 1 is in the correct place
        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1 and element 2,
            #   to the right by 1
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1


# Now going to do the sorting inplace.
#   "l" is for the left (start) index,
#   "r" is for the right (end) index
#   of the sub-array of the array to be sorted.
def merge_sort_in_place(arr, l, r):
    # If the left (start) is less than the right (end)
    if l < r:

        # Want to do floor divide by 2 to avoid overflow for large l and r
        m = (l + (r - 1)) // 2

        # Sort the first half
        merge_sort_in_place(arr, l, m)

        # Sort the second half
        merge_sort_in_place(arr, m + 1, r)

        # Merge both sorted halves back together
        merge_in_place(arr, l, m, r)
