"""
Input: a List of integers
Returns: a List of integers
"""

# ### Solution code from 1st group ### #
# # First-pass solution (make it work!)
# def moving_zeroes(arr):
#     for i in arr:  # Iterate through the values in array
#         if i == 0:  # If the value is 0
#             arr.remove(i)  # Remove the 0
#             arr.append(0)  # Add the 0 to the end of the array
#     return arr  # Close the loop by returning the new array


# ### Joseph's code (2nd Evening Group) ### #
# # First Pass Solution
# def moving_zeroes(arr):
#     # Find the non-zero integer in given list of integers
#     for num in arr:
#         if num != 0:  # If the num is not a 0
#             # Move each non-zero integer to the
#             #   LEFT side of the array
#             # Just continue here, don't need to move anything
#             continue
#
#         else:  # num will be a 0
#             # Move each zero integer to the
#             #   RIGHT side of the array
#             arr.append(num)  # Adds the num to the end
#             arr.remove(num)  # Removes the num from current index
#                 # Remove is a for loop under the hood:
#                 # for i in arr:
#                 #    if i == num:
#                 #        del arr[i]
#     # Return the sorted list of integers
#     return arr


# # 2nd pass solution
# def moving_zeroes(arr):
#     # bucket = [0] * len(arr)  # One way to create a bucket
#     bucket = [0 for _ in arr]  # Another way to create a bucket
#     counter = 0  # Create a counter
#
#     for num in arr:  # for each num in arr
#         if num != 0:  # if the num is not 0
#             bucket[counter] = num  # moves the non-zero int left
#             counter += 1  # Increment the counter for next iteration
#
#     return bucket


# # Chaz's 2nd pass solution
# def moving_zeroes(arr):
#     # Create a bucket that holds all non-zero integers
#     bucket = [num for num in arr if num != 0]
#     # Add 0's to the end of the bucket for the remaining length of the array
#     bucket += [0] * (len(arr) - len(bucket))
#     # Return the bucket with the sorted integers
#     return bucket

# Fatima's 1st pass (Feb 2021 session):
def moving_zeroes(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right += 1

        else:
            if arr[left] != 0:
                left += 1

            if arr[right] == 0:
                right -= 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
