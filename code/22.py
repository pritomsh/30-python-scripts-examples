# Define a function that takes  arguments you can use one or more than one arguments  and returns them
# you can sum , divide, or do any operation you want 
#here i do a sum operation
def add_numbers(num1, num2):
    sum = num1 + num2
    return  sum

# Call the function and print the result
result = add_numbers(5, 5)
print(result)  

#in this Function this is print User name 
def showName(name):
    print("Welcome to Dada's Club : {}".format(name))

showName("Pritom")

#you can take input user than show this 
name2 = input("Enter your name :")
showName(name2)



'''
10
Welcome to Dada's Club : Pritom
Enter your name :Himel
Welcome to Dada's Club : Himel
'''