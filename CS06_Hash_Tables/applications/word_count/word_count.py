def word_count(s):
    counters = {}
    word_list = s.lower().split()
    for word in word_list:
        word = word.strip('":;,.-+=/\\|[]}{()*^&’')
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1
    # print(word_list)
    return counters



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))