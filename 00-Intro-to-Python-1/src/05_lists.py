# For the exercise, look up the methods and functions that are available for use
# with Python lists.
# An array can only have one data type, list can have multiple data types.
# If you want to add to an array you have to create a new array twice the size of the one you have, taking up more space.
# You need to use numpy to use arrays or it will just be a list in python.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.pop(4)  # pop(index #)
# x.pop(-3)
# x.remove(8)  # computationally more expense
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)  # insert(index place where to insert, value)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
# Using a for loop will print each number individually
# for num in x:
#     print(num * 1000)
# Same thing as above but in List Comprehension which will print it as a list - similar to .map in JS
x = [num * 1000 for num in x]
print(x)

# Can also do it as a list of strings instead of integers:
# x = [str(num * 1000) for num in x]
# print (x)
