# 1: Create a generator function that takes a positive integer n as input and 
# generates all the even numbers up to and including n.
from collections.abc import Iterator

def even_numbers(number: int) -> Iterator[int]:
    for num in range(0, number+1, 2):
        yield num

gen = even_numbers(70)
for num in gen:
    print(num)
