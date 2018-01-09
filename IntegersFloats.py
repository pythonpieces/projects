# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2﻿

# prints <class 'int> for a class integer which is a number. num = 3.14 gives you a class float <class 'float'.
num = 3
print(type(num))

num = 3.14
print(type(num))
###################
print(2 % 2)
print(3 % 2)
print(4 % 2)
print(5 / 2) # prints a float of 2.5 in python3 and not in python2
print(6.4 // 2) # prints 3.0

# increment +=
num = 1
num += 1
print(num) # prints 2


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num_1 = 3
num_2 = 2
print(num_1 == num_2) # False
print(num_1 != num_2) # True
print(num_1 > num_2) # True
print(num_1 < num_2) # False
print(num_1 >= num_2) # True
print(num_1 <= num_2) # False

# casting
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2) # outputs 300

num_3 = '100.8'
num_4 = '200.6'

num_3 = float(num_3)
num_4 = float(num_4)

print(num_3 + num_4) # outputs 301.4