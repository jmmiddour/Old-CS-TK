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

from collections import deque

def sliding_window_max(nums, k):
    max_list = []
    dq = deque()




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
