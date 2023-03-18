# To add an item to a list, you can use the append() method:
my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list)  # [1, 2, 3, 4, 5]

# Alternatively, you can use the insert() method to add an item at a specific index:
my_list = [1, 2, 3, 4]
my_list.insert(2, 2.5)
print(my_list)  # [1, 2, 2.5, 3, 4]


# To remove an item from a list, you can use the remove() method to remove the first occurrence of a specific value:
my_list = [1, 2, 3, 4]
my_list.remove(2)
print(my_list)  # [1, 3, 4]

#You can also use the pop() method to remove an item at a specific index and return its value:
my_list = [1, 2, 3, 4]
removed_item = my_list.pop(2)
print(my_list)  # [1, 2, 4]
print(removed_item)  # 3

