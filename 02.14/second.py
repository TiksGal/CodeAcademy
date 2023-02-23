def add_string_ending(list:str, ending:str) ->str:
    new_list = [f"{fruits}{ending}" for fruits in list]
    return new_list

fruits = ["apple", "banana", "cherry", "rasbery", "watermelon"]
print(add_string_ending(fruits, "s"))