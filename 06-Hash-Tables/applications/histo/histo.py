# Your code here
def histo():
    with open('robin.txt', 'r') as file_out:
        data = file_out.read()

    # Create an array from the data
    words = data.split()
    cache = {}

    for word in words:
        word = word.lower().strip('":;,.-+=/\\|[]}{()*^&')

        if word not in cache:
            cache[word] = []

        else:
            cache[word].append('#')

    return cache