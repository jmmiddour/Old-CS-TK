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
# First Pass Solution
def moving_zeroes(arr):
    # Find the non-zero integer
    if num != 0:
    # Move each non-zero integer to the LEFT side of the array
    # Move each zero integer to the RIGHT side of the array
    # Return the sorted list of integers

# 2nd pass solution
def moving_zeroes(arr):
    # bucket = [0] * len(arr)  # One way to create a bucket
    bucket = [0 for _ in arr]  # Another way to create a bucket
    counter = 0

    for num in arr:
        if num != 0:
            bucket[counter] = num
            counter += 1

    return bucket


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")