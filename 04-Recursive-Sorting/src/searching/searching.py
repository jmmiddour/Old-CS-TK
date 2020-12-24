# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # If end of array is greater than or equal to, need equal in case target is there
    if end >= start:
        # Get the value in the middle of the array
        middle = (start + end) // 2

        # If target equals the value in the middle of the array
        if target == arr[middle]:
            # Return the middle of the array, target is now found
            return middle

        # If target is greater than the valie in the middle of the array
        elif target > arr[middle]:
            # Return the function with the middle value as the start - 1 to match the index
            return binary_search(arr, target, (middle -1), end)

        # If the target is less than the value in the middle of the array
        elif target < arr[middle]:
            # Return the function with the middle value as the end -1 to match the index
            return binary_search(arr, target,start,(middle - 1))

    # If the target is not found, return -1 per the tests
    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
