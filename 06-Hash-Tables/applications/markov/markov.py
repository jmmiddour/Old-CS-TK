import random


# TODO: analyze which words can follow other words
def markov(words):
    cache = {}
    word_list = words.split()

    for i in range(len(word_list) - 1):
        word = words_split[i].lower().strip('":;,.!?-+=/\\|[]}{()*^&')
        next_word = words_split[i +1].lower().strip('":;,.!?-+=/\\|[]}{()*^&')

        if word not in cache:
            cache[word] = {}

        if next_word not in cache[word]:
            cache[word][next_word] = 0

        cache[word][next_word] += 1

    for word in cache:
        next_words = cache[word]
        total = 0

        for word in next_words:
            count = next_words[word]
            total += count

        for word in next_words:
            next_words[word] /= total

    return cache


# TODO: construct 5 random sentences
# Your code here

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    chain = markov(words)

    counter = 0
    while counter < 5:
        counter += 1
        sentence = ['the']

        while len(sentence) < 8:
            rand_num = random.random()

            word = sentence[-1]
            total = 0

            for next_word in chain[word]:
                total += chain[word][next_word]

                if total > rand_num:
                    sentence.append(next_word)
                    break

print(' ').join
