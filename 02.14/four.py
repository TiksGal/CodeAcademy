def unique_strings(str_list: str) ->str:
    unique_str = []
    for s in str_list:
        if len(set(s)) == len(s):
            unique_str.append(s)
    return unique_str

strings = ["hello", "world", "python", "unique", "characters"]
unique = unique_strings(strings)
print(unique)

