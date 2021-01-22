"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""

# When you are solving a problem there are 3 phases:
# 1. Make it work!
# 2. Make it fast!
# 3. Make it pretty!
# The root of all evil --> Premature Optimization!!!

# The UPER Method:
# Understand --> Read the question/problem CAREFULLY!
# Plan --> Write your Pseudocode!
# Execute/Enact --> Write the code!
# Refactor/Review/Reflect --> How can I make it better?


# ### Solution from 1st Group ### #
# # First-pass solution (just make it work):
# def single_number(arr):
#     stack = {}  # Need to create an empty dictionary to store pairs
#     for char in arr:  # Iterate through the array
#         if char in stack:  # Iterate through the stack to match values
#             stack[char] += 1  # If values match increase stack value by 1
#         else:
#             stack[char] = 1  # If values do not match the stack value is just 1
#
#     for key, val in stack.items():  # Get the keys and values from the stack
#         if val == 1:  # If the value is 1
#             return key  # Return the key value


# ### Sam's code (2nd Evening Session)... ### #
# # First Pass Solution:
# def single_number(arr):
#     # Start with dictionary
#     dic = {}
#     # Loop through array
#     for num in arr:
#         # If the number is not currently in dictionary, make new key there = 1 (acting as a counter)
#         if num not in dic:
#             dic[num] = 1
#         # If it is in the dictionary, increase count
#         else:
#             dic[num] += 1
#     # Loop through the dictionary for wherever the value is 1
#     for key in dic:
#         if dic[key] == 1:
#             # Return the key in the dictionary where the value is 1
#             return key
# # ^-- Time Complexity = O(n^2)

# # Second pass solution
# def single_number(arr):
#     dic = {}
#     # arr_list = []
#
#     for num in arr:
#         if dic.get(num):
#             del dic[num]
#         else:
#             dic[num] = 1
#
#     return next(iter(dic.keys()))  # dic.keys()


# Doc's SUPER solution
def single_number(arr):
    ans = 0
    for x in arr:
        ans ^= x  # Bitwise operator

    return ans


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")