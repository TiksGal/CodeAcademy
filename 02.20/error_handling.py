# Create a function that takes one parameter as number - age , other as name which is default 
# 'Anatnas', and some args and keywords.
# Print first Name with age;
# And then print all arguments with key arguments.


def info(age: int, name: str = "Antanas", *args, **kwargs) -> None:
    print(f"{name} is {age} years old.")
    print(f"free arguments: {args if args else 'No args'}, free key arguments: {kwargs if kwargs else 'No kwargs'}")
# print(f"{args} {kwargs}") if args and kwargs != None else print("Add args and kwargs")
info(30, "Antanas", "Male", "Engineer", location="Vilnius", hobbies=["basketball", "hiking"])

# from typing import Any, List


# def print_info(age: int, name: str = 'Anatnas', *args: Any, **kwargs: Any) -> None:
#     print(f"{name} is {age} years old.")
#     print("Additional information:")
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
        
# The function takes an integer age as the first argument and an optional string name as the 
# second argument, which defaults to 'Anatnas'. The *args parameter allows any number of additional
# positional arguments of any type, while the **kwargs parameter allows any number of additional 
# keyword arguments of any type. The function returns None.
# The implementation is very similar to the previous one, but with added type annotations and simpler 
# variable names. The for loops iterate over args and kwargs.items() respectively, printing each item in turn.

# print_info(30, "John", "Male", "Software Engineer", location="New York", hobbies=["reading", "hiking"])
