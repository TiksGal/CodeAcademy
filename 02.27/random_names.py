import random
from py_random_words import RandomWords

rng = RandomWords()

# Generate 5 random words
words = []
for i in range(5):
    word = rng.get_word()
    words.append(word.upper())

# Sort the words
words.sort()

print(words)