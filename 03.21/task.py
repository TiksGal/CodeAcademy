# write a python script that adds all the numbers entered in the command line as arguments. 
# Throw an error if user enters something other than number
import sys

sum = 0

for arg in sys.argv[1:]:
    try:
        sum += float(arg)
    except ValueError:
        print("Error: Wrong argument entered")
        sys.exit(1)


print("Sum of the numbers entered is:", sum)