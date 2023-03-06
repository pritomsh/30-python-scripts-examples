'''
use %f formatter to specify the number of decimal numbers to be returned when a floating point number is rounded up.
'''

# Use of String Formatting
number1 = 563.78453
print("{:.2f}".format(number1)) # 2 decimal place

# Use of String Interpolation
number2 = 563.78453
print("%.3f" % number2) # 3 decimal place 



'''
Output:

563.78
563.785
'''