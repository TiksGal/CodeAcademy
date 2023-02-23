import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# logging.basicConfig(level=logging.DEBUG,filename='first.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

def log_message(message: str) -> None:
    logging.info(message)

while True:
    try:
        input_str = input("Enter your text here: ")
        if input_str == "quit":
            break
        if "." in input_str:
            input_val = float(input_str)
        else:
            input_val = int(input_str)
        log_message(f"User input: {input_val}")
    except ValueError as e:
        log_message(f"Invalid input: {input_str}. Error: {str(e)}")
    except KeyboardInterrupt:
        log_message("Program stopped by user")
        break
    except Exception as e:
        log_message(f"Unexpected error: {str(e)}")
    