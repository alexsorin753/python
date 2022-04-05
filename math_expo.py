import math

def my_function(num, exp):
    pow = math.pow(num, exp)
    return ("%.17f" % pow).rstrip('0').rstrip('.')

print(my_function(118, 13))