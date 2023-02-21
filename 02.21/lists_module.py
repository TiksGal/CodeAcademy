def remove_duplicates(lst: list) ->list:
    """Return a new list with duplicate elements removed"""
    return list(set(lst))

def find_common_elements(lst1, lst2):
    """Return a list of common elements between two input lists"""
    return list(set(lst1) & set(lst2))