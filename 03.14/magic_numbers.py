def is_magic_number(num: int) -> bool:
    if num <= 9:
        return num == 1
    else:
        sum_of_digits = 0
        while num > 0:
            sum_of_digits += num % 10
            num //= 10
        return is_magic_number(sum_of_digits)
    
    
print(is_magic_number(1234))