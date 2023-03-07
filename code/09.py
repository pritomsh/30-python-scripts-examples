#enter age if you are 18 years or more than you can vote 

age = int(input("Enter age"))

# the test condition is always True
while age > 18:
    print('You can vote')

else:
    print("You can't vote")

