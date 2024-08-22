#creating an empty list

my_list = []
print(f"My empty list:", my_list)

#append the list
my_list.append (10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"My appended list:", my_list)

#insert into the list
my_list.insert(1, 15)
print(my_list)

#extend the list
my_list.extend([50,60,70])
print(f"My extended list:", my_list)

#remove from the list
my_list.pop()
print(f"Ammended list:", my_list)

#Sort the list
my_list.sort()
print(f"Sorted list", my_list)

#Print the index
index_30 = my_list.index(30)
print(f"Index for number 30:", index_30)