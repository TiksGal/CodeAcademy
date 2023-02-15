# Write a function that takes two lists and 
# adds the first element in the first list with the first element in the second list,
# the second element in the first list with the second element in the second list, 
# etc, etc. Return True if all element combinations add up to the same number. Otherwise, 
# return False.
list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]

def add_lists(list1: list[int], list2: list[int]) -> bool:
    sum1: int = sum(list1)
    sum2: int = sum(list2)
    total_sum: int = sum1 + sum2
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] + list2[i] != total_sum / len(list1):
            return False
    return True

print(add_lists(list1, list2))