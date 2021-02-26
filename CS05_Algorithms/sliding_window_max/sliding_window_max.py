"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""

# ### Livy's Code (2nd Morning Session)... ### #
# # First Pass Solution
# def sliding_window_max(nums, k):
#     # Create a max array to store each max number
#     max_arr = []
#     # Create current_i = 0
#     current_i = 0
#     # Iterate through the array
#     while k <= len(nums):
#         # Create window variable == nums[current_i:k]
#         window = nums[current_i]
#         # Find max value in the window
#         max_value = max(window)
#         # Append max value to max array
#         max_arr.append(max_value)
#         # Increment current index
#         current_i += 1
#         # Increment k
#         k += 1
#     # Return max array
#     return max_arr

# from collections import deque
#
# def sliding_window_max(nums, k):
#     max_list = []
#     dq = deque()


# ### My Code (2nd Evening Session)... ### #
# # First pass solution
# def sliding_window_max(nums, k):
#     # nums <-- list of integers
#     # k <-- single integer (size of the window)
#     # Create a list to store the largest numbers
#     max_vals = []
#
#     # Iterate through nums k numbers at a time
#     for i in range(len(nums) - k + 1):
#         # window = nums([i:i + k])  # Set the window size
#         # largest = max(window)  # Grab the largest value in current window
#         # max_vals.append(largest)  # Adds the largest value to the end of max_vals
#         max_vals.append(max(nums[i:i + k]))  # Chaz's version of above
#
#     return max_vals


# Second pass solution (Chaz's solution - 2nd Evening Group)
def sliding_window_max(nums, k):
    # nums <-- list of integers
    # k <-- single integer (size of the window)
    # Create a list to store the largest numbers
    max_vals = [0] * (len(nums) - k + 1)

    # Iterate through nums k numbers at a time
    for i in range(len(nums) - k + 1):
        max_vals[i] = max(nums[i:i + k])  # This takes the place of append in 1st pass

    return max_vals


# # Second pass solution (Doc's solution - 2nd Evening Group)
# from collections import deque
#
# def sliding_window_max(nums, k):
#     # nums <-- list of integers
#     # k <-- single integer (size of the window)
#     # Create a list to store the largest numbers
#     maxes = []
#     # Use deque
#     dq = deque()
#     # Instead of range(), use enumerate()
#     # Use the methods: pop(), append(), and pop_left()
#     # Use a while loop inside a for loop
#     # Use pop() inside the while loop
#
#     return None  # None is just a placeholder for now


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
