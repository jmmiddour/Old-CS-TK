"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
y = [num for num in range(1, 6)]
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
y = [num ** 3 for num in range(10)]
print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".
a = ["foo", "bar", "baz"]
y = [word.upper() for word in a]
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.
x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
# y = [x[:len(x) + 1:2]]  # This is a way to step using slicing
#      ^-- will print every other index value starting with the first number
y = [i for i in x if int(i) %2 == 0]
print(y)

# Get user input and print just one number and word or sentence
num = int(input("Type a number:"))
print(num)
print(num * 3)
word = input("Type a word or sentence:")
print(word)


# To have a user enter multiple numbers then output a list of single numbers
c = []
y = input("Enter numbers:")

# Using a regular for loop
# for letter in y:
#     num = int(letter)
#     c.append(num)

# Using list comprehension
c = [int(letter) for letter in y]
print(c)