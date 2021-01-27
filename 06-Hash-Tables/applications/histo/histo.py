# # Your code here
# def histo():
#     with open('robin.txt', 'r') as file_out:
#         data = file_out.read()
#
#     # Create an array from the data
#     words = data.split()
#     cache = {}
#
#     for word in words:
#         word = word.lower().strip('":;,.-+=/\\|[]}{()*^&')
#
#         if word not in cache:
#             cache[word] = []
#
#         else:
#             cache[word].append('#')
#
#     return cache


# Fatima's Code (2nd morning session)... ###
def histo(text):
    with open(text, 'r') as file_out:
        data = file_out.read()

    # Create an array from the data
    words = data.split()
    cache = {}

    for word in words:
        word = word.lower().strip('":;,.-+=/\\|[]}{()*^&')

        if word not in cache:
            cache[word] = []

        cache[word].append('#')

    for word, count in cache.items():
        # print('{/s:>20}{/s:>100}'.format(word, count))
        print(f"{word:20} {''.join(count)}")

    return cache

histo('robin.txt')
