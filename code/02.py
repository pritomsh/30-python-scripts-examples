#  add More than two strings can be concatenated using ‘+’ operator.
# make full name using first name and last name

f_name = "Pritom"
l_name = "Saha"
full_name = f_name+ " " + l_name
print("Full Name :",full_name)

'''
Output:
Pritom Saha
'''

'''
Using format()
The format() is a string formatting function used to concatenate two strings.
''' 

namef="Himel"
namel="Saha"
fname="Full name : {} {}".format(namef,namel)

print(fname)

'''
Output:

Full Name : Pritom Saha
Full name : Himel Saha
'''