from operator import*
list1 = [1, 2, 3, 4, 5]
m = 1
for i in list1:
  # multiplying all elements in the given list
  # using mul function of operator module
    m = mul(i, m)
# printing the result
print(m)