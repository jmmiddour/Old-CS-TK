from dis import dis  # Gives you a breakdown of what your computers is doing (execution stack)


# Write a function is_even that will return true if the passed-in number is even.
# YOUR CODE HERE
def is_even(num):
    return num %2 == 0

print(is_even(7))
print(is_even(8))

# Read a number from the keyboard
num = int(input("Enter a number: "))
# num = int(num)


# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE
def print_even(num):
    if num % 2 == 0:
        print('Even!')
    else:
        print('Odd')


print(print_even(num))

dis(print_even)  # breaks down what the print_even function is doing under the hood
