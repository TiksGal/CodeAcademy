# You are given an input array of bigrams, and an array of words. Write a function that returns True 
# if every single bigram from this array can be found at least once in an array of words.

bigrams = input("Enter the bigrams, separated by spaces: ").split()
words = input("Enter the words, separated by spaces: ").split()

from typing import List

def check_bigrams(bigrams: List[str], words: List[str]) -> bool:
    for bigram in bigrams:
        found = False
        for word in words:
            if bigram in word:
                found = True
                break
        if not found:
            return False
    return True

print(check_bigrams(bigrams, words))