# create an empty list 
my_list = []

# append elements to the list 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert value 15 at second position in the list
my_list.insert(1, 15)

# extend the list with another list
my_list.extend([50, 60, 70])

# remove the last element
my_list.pop()

# sort in the ascending order
my_list.sort()

# find and print the index of the value 30
index_of_30 = my_list.index(30)
print(f"The index of 30 in the list is: {index_of_30}")
