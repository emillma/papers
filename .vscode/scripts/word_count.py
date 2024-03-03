import sys


text = sys.argv[1]


def count_words(text):
    return len(text.split())


print(count_words(text))
