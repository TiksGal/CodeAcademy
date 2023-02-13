# Create a list of letters and generate 5 diferent words for 5 different lists. (A word must the size between 5 and 15 letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.

import random
import string

word_lists = []
for i in range(5):
    words = []
    for j in range(5):
        word = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 15)))
        words.append(word)
        word_lists.append(words)
        
words = ["".join(random.choices(string.ascii_letters, k=random.randint(5, 15))) for _ in range(5)]
letter_counts = {}
for word in words:
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

print("Words:", word_lists)
print("Letter counts:", letter_counts)
