from typing import Any

def check_arguments(mandatory: Any,  *args, **kwargs) -> None:
    print (mandatory)
    if args:
        print (args)
    if kwargs:
        print (kwargs)
        
check_arguments(1, 2, 2, 4, 5, lalal = "salal")