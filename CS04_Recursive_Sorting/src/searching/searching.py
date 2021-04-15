# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # # If end of array is greater than or equal to, need equal in case target is there
    # if start > end:
    #     # Get the value in the middle of the array
    #     middle = (start + end) // 2
    #
    #     # If target equals the value in the middle of the array
    #     if target == arr[middle]:
    #         # Return the middle of the array, target is now found
    #         return middle
    #
    #     # If target is greater than the value in the middle of the array
    #     elif target > arr[middle]:
    #         # Return the function with the middle value as the start - 1 to match the index
    #         return binary_search(arr, target, (middle -1), end)
    #
    #     # If the target is less than the value in the middle of the array
    #     elif target < arr[middle]:
    #         # Return the function with the middle value as the end -1 to match the index
    #         return binary_search(arr, target, start, (middle - 1))
    #
    # # If the target is not found, return -1 per the tests
    # return -1

    #########################################################################
    ################## New Solution - Previous not passing ##################
    #########################################################################
    mid = (start + end) // 2

    if start > end:
        return -1

    if arr[mid] == target:
        return mid

    elif target > arr[mid]:
        return binary_search(arr, target, mid + 1, end)

    elif target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     if arr[0] < arr[-1]:
#         return binary_search(arr, target, 0, len(arr) - 1)
#
#     else:
#         left = 0
#         right = len(arr) - 1
#
#         while left <= right:
#             mid = left + right // 2
#
#             if arr[mid] == target:
#                 return mid
#
#             elif arr[mid] < target:
#                 right = mid - 1
#
#             else:
#                 left = mid + 1
#
#         return -1

########################################################################
###################### Fixing Errors in above code #####################
########################################################################
# def agnostic_binary_search(arr, target, start=0, end=-1):
#     asc_arr = []
#
#     if arr is None:
#         return -1
#
#     elif len(arr) <= 2 and (start != target or end != target):
#         return -1
#
#     if start > end:
#
#         asc_arr.append(arr[::-1])
#         return agnostic_binary_search(asc_arr, target, asc_arr[0], asc_arr[-1])
#
#     # elif start > end:
#
#     elif start < end:
#         return binary_search(arr, target, start, end)


#######################################################################
############## Christopher's Code - Infinate loop Problem #############
#######################################################################

# def agnostic_binary_search(arr, target, low = 0, high = -1):
#     if arr != sorted(arr):
#         arr = arr[::-1]
#
#     if high == -1:
#         high = len(arr)
#
#     current = (low + high) // 2
#
#     print(f"Current: {current}")
#
#     if arr[current] == target:
#         return current
#
#     elif len(arr[low: high]) <= 1:
#         return -1
#
#     # elif (arr[current] > arr[current - 1] and arr[current] < target) or (
#     #         arr[current] < arr[current - 1] and arr[current] > target):
#     elif arr[current] > target:
#         return agnostic_binary_search(arr, target, current + 1, -1)
#
#     elif arr[current] < target:
#         return agnostic_binary_search(arr, target, 0, current - 1)

#######################################################################
##############   Christopher's Code - Working Solution   ##############
#######################################################################

def agnostic_binary_search(arr, target, low = 0, high = -1):
    if high == -1:
        high = len(arr)

    current = (low + high) // 2

    # print(f"Current: {current}")

    if arr[current] == target:  # found the target
        return current

    elif low > high:  # target is not in array
        return -1

    elif (arr[len(arr)-1] > arr[0]):  # array is in ascending order
        if arr[current] < target:
            return agnostic_binary_search(arr, target, current + 1, high)

        else:
            return agnostic_binary_search(arr, target, 0, current - 1)

    else:  # array is in descending order
        if arr[current] > target:
            return agnostic_binary_search(arr, target, current + 1, high)

        else:
            return agnostic_binary_search(arr, target, 0, current - 1)


if __name__ == '__main__':
    ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
    descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]

    agnostic_binary_search(ascending, 2)
    agnostic_binary_search(descending, 49)