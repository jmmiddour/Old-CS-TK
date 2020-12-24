'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


# First-pass solution (just make it work):
def single_number(arr):
    stack = {}  # Need to create an empty dictionary to store pairs
    for char in arr:  # Iterate through the array
        if char in stack:  # Iterate through the stack to match values
            stack[char] += 1  # If values match increase stack value by 1
        else:
            stack[char] = 1  # If values do not match the stack value is just 1

    for key, val in stack.items():  # Get the keys and values from the stack
        if val == 1:  # If the value is 1
            return key  # Return the key value





if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")