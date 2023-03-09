'''
for itarator_variable in sequence_name:
	Statements
	. . .
	Statements
'''

weekdays = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
print("Seven Weekdays are:\n")
# Iterate the list using for loop
for day in range(len(weekdays)):
    print(weekdays[day])
    #With the break statement we can stop the loop before it has looped through all the items:
    if day == 3: 
        break
