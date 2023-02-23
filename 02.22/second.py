import logging

logging.basicConfig(level=logging.DEBUG,filename='second.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')



def log_message(message: str) -> None:
    logging.info(message)

def is_int(elem):
    try:
        int(elem)
        return True
    except ValueError:
        return False

def move_to_end(lst, value):
    log_message(f"Input list: {lst}")
    log_message(f"Value to move: {value}")

    if not all(is_int(elem) for elem in lst):
        log_message(f"Invalid input: {lst}. List elements must be integers.")
        raise ValueError("List elements must be integers.")
    
    if not is_int(value):
        log_message(f"Invalid input: {value}. Value to move must be an integer.")
        raise ValueError("Value to move must be an integer.")
    
    i = 0
    j = len(lst) - 1
    
    while i < j:
        if lst[i] == value:
            lst[i], lst[j] = lst[j], lst[i]
            j -= 1
        else:
            i += 1
    
    log_message(f"Output list: {lst}")
    return lst

try:
    input_lst = input("Enter a list of integers, separated by commas: ")
    lst = input_lst.split(",")
    input_val = input("Enter a value to move to the end: ")
    
    result = move_to_end(lst, input_val)
    print(f"Result: {result}")
    
except ValueError as e:
    print(f"Error: {str(e)}")
    log_message(f"Error: {str(e)}")
    
except Exception as e:
    print(f"Unexpected error: {str(e)}")
    log_message(f"Unexpected error: {str(e)}")