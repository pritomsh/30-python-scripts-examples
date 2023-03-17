'''A list comprehension is a way to create a new list based on an existing list using a single line of code
Basic syntax 

new_list = [expression for item in iterable if condition]

'''

squares = [x**2 for x in range(1, 11)]
print(squares)  

# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


odds = [x for x in range(1, 11) if x % 2 != 0]
print(odds)  

# Output: [1, 3, 5, 7, 9]


name = 'Pritom Saha'
print( [ newN for newN in name if len(name)>10 ])

# Output: ['P', 'r', 'i', 't', 'o', 'm', ' ', 'S', 'a', 'h', 'a']