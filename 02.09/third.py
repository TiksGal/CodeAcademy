# Create a list of letters and generate 5 diferent words for 5 different lists. (A word must the size between 5 and letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.

import random
import string

words = ["".join(random.choices(string.ascii_letters, k=random.randint(5, 15))) for _ in range(5)]
letter_counts = {}
for word in words:
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

print("Words:", words)
print("Letter counts:", letter_counts)
