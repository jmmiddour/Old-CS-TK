'''
Input: a List of integers
Returns: a List of integers
'''


# First-pass solution (make it work!)
def moving_zeroes(arr):
    for i in arr:  # Iterate through the values in array
        if i == 0:  # If the value is 0
            arr.remove(i)  # Remove the 0
            arr.append(0)  # Add the 0 to the end of the array
    return arr  # Close the loop by returning the new array

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")