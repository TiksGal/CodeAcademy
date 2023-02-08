# Python code to demonstrate
# addition of two list
# list comprehension
 
# initializing lists
test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]

 
# using list comprehension to
# add two list
res_list = [test_list1[i] + test_list2[i] for i in range(len(test_list1))]
 
# printing resultant list
print ("Resultant list is : " + str(res_list))