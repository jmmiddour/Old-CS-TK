"""
Input: a List of integers
Returns: a List of integers
"""


# ### Solution from first study group ### #
# First-pass solution (just make it work!)
# def product_of_all_other_numbers(arr):
#     output = [0 for i in range(len(arr) - 1)]  # Creates an empty array
#
#     temp = []  # Will hold values that are not the index value
#
#     for i in range(len(arr)):
#         arr_i = i  # Will hold the array index value


# ### Livy's Code (2nd Morning Session)... ### #
# import math
# # First Pass Solution
# def product_of_all_other_numbers(arr):
#     # Create an empty array for single numbers
#     nums = []
#     # Create an empty array for products of numbers
#     products = []
#
#     # Iterate through the array to get single number (x)
#     for x in arr:
#         # Iterate through array again to get numbers (y)
#         for y in arr:
#             # Check if x from the 1st array is equal to y
#             if x == y:
#                 # Ignore x
#                 continue
#
#             else:
#                 # Find the product of all the numbers excluding x
#                 product = math.prod(nums)  # Math method that returns the product
#                 # Empty out nums array
#                 nums = []
#                 # Append product variable to array
#                 products.append(product)
#
#         return products


# ### Fatima's code (2nd Morning Session)... ### #
# # 2nd pass solution
# def product_of_all_other_numbers(arr):
#     current_index = 0
#     all_products = []
#     product = 1
#
#     for num in arr:
#         for i in range(len(arr)):
#             if current_index == i:
#                 pass
#             else:
#                 product *= arr[i]
#         all_products.append(product)
#         current_index += 1
#         product = 1
#     return all_products


# ### Theda's Code (2nd Evening Session)... ### #
# # First pass solution
# def product_of_all_other_numbers(arr):
#     # Multiply all numbers except the current value
#     product_bucket = [0] * len(arr)  # holds all products
#     current_val = 1  # will hold the current value
#
#     # Check to make sure arr is not empty
#     if arr[0] is None:
#         return None
#
#     for i in range(len(arr)):  # Track where we are in the product bucket
#         for j in range(len(arr)):  # Track where we are in the arr
#             if i != j:  # If i does not equal j
#                 current_val *= arr[j]  # Multiply all values (not at arr index)
#                 #                          make that the new current value
#         # Assign the new current value to the product bucket for that index
#         product_bucket[i] = current_val
#         # Reset the current value to 1
#         current_val = 1
#
#     # Return all the products
#     return product_bucket


# ### Ava's Code (2nd Evening Session)... ### #
from math import prod
# # 2nd pass solution
# def product_of_all_other_numbers(arr):
#     product = prod(arr)  # holds the product of the arr at index
#     product_bucket = [1] * len(arr)  # holds all the products
#
#     if arr[0] is None:  # Checks to make sure not an empty arr
#         return None
#
#     for i in range(len(arr)):  # Iterate through the length of arr
#         # Assigns the product / arr index value to the product bucket
#         product_bucket[i] = product[i] / arr[i]
#
#     return product_bucket


# ### Doc's code (2nd Evening Session)... ### #
# 2nd pass solution
def product_of_all_other_numbers(arr):
    products = [0 for _ in range(len(arr))]
    products_so_far = 1

    for i in range(len(arr)):
        products[i] = products_so_far
        products_so_far *= arr[i]

    products_so_far = 1

    # Start at end, stop at -1, step -1
    #   ^-- This will move backwards through the list
    for i in range(len(arr) - 1, -1, -1):
        products[i] *= products_so_far
        product_so_far *= arr[i]

    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
