# Create a function that takes a list of integers, sums the even and odd numbers separately, 
# then returns the difference between the sums of the even and odd numbers. 

from typing import List

def sum_even_odd_numbers(numbers: List[int]) -> int:
    even_sum: int = 0
    odd_sum: int = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    if even_sum > odd_sum:
        return even_sum - odd_sum
    else:
        return odd_sum - even_sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum_even_odd_numbers(numbers))