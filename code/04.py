import math

number = 4
powr = 3

# Method 1
power = number ** powr
print("%d to the power %d is %d" % (number, powr, power))

# Method 2
power = pow(number, powr)
print("%d to the power %d is %d" % (number, powr, power))

# Method 3
power = math.pow(number, powr)
print("%d to the power %d is %5.2f" % (number, powr, power))