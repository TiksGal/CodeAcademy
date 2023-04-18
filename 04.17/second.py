# Create a generator function that would pick word from a generator and/list of generated random words (should be > 10000) and would stop itterating
# until the word longer than 7 lettters is found.
# Compare sizes of list and generator. Calculate performance per both executions (time to complete in ms)

import random
import string
import timeit
from sys import getsizeof


def random_word_generator():
    while True:
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 10)))
        yield word


def find_long_word(word_iterable):
    for word in word_iterable:
        if len(word) > 7:
            return word


word_list = [''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 10))) for _ in range(10000)]
word_generator = random_word_generator()

list_size = getsizeof(word_list)
generator_size = getsizeof(word_generator)
print(f"Size of list: {list_size} bytes")
print(f"Size of generator: {generator_size} bytes")

list_time = timeit.timeit(lambda: find_long_word(word_list), number=10000) * 1000
generator_time = timeit.timeit(lambda: find_long_word(word_generator), number=10000) * 1000
print(f"Time for list: {list_time:.2f} ms")
print(f"Time for generator: {generator_time:.2f} ms")







