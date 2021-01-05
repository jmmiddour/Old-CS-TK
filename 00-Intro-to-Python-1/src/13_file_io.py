"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
# If you use a context manager (`with open()`) you do not need to close
#   the file because it will automatically close it for you.
# YOUR CODE HERE
text = open("./foo.txt", "r")
print(text.read())
text.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bartxt = open('bar.txt', 'w')  # a+ creates and adds to file
bartxt.write('The cat \nknows a lot\nabout that.')
bartxt.close()

# r+ : - Open for reading and writing.
# The stream is positioned at the beginning of the file.

# a+ : - Open for reading and writing.
# The file is created if it does not exist.
# The stream is positioned at the end of the file.
# Subsequent writes to the file will always end up at the then current
#   end of file, irrespective of any intervening fseek(3) or similar.
