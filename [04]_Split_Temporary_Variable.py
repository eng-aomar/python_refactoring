# -------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------  Split Temporary Variable-------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# [Problem] : You have a local variable that’s used to store various intermediate values inside a method (except for cycle variables)
# [Solution] :Use different variables for different values. Each variable should be responsible for only one particular thing.
# -------------------------------------------------------------------------------------------------------------------------------------

from math import pi

# [Problem] : You have a local variable that’s used to store various intermediate values inside a method (except for cycle variables)
r = 5
temp = 2 * pi * r
print('-' * 50)
print('perimeter =', temp)
print('-' * 50)
temp = pi * r ** 2
print('area =', temp)
print('-' * 50)

# [Solution] :Use different variables for different values. Each variable should be responsible for only one particular thing.

r = 5
perimeter = 2 * pi * r
print('-' * 50)
print('perimeter =', perimeter)
print('-' * 50)
area = pi * r ** 2
print('area =', area)
print('-' * 50)
