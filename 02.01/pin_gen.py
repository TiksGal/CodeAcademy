pin = 7801

i = 0
while True:
    if i != pin:
        i += 1
    else:
        print("Your pin code is:", pin)
        break