def is_leap(metai)-> bool:
    if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_leap(2000))
    print(is_leap(2020))
    print(is_leap(2100))

