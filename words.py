from copy import deepcopy

def get_wordlist():
    with open(r"words.txt", 'r') as fp:
        for count, line in enumerate(fp):
            pass
    file = open('words.txt')
    words = list(range(count))
    for i in range(count):
        words[i] = file.readline().strip()
    file.close()
    return words

def check_word(word, letters):
    letters_copy = deepcopy(letters)
    for c in word:
        for i in range(len(letters_copy)):
            if c == letters_copy[i]:
                letters_copy[i] = 0
                break
            elif i == len(letters_copy) - 1: return False
    return True