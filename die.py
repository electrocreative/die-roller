"""
A simple die roller

Author: Scott R. Henz
Date: 09/02/2022
"""

import random

first = int(input('Type the first number: '))
last = int(input('Type the last number: '))
roll = random.randint(first, last)

print('Choosing a number between ' + str(first) + ' and ' + str(last) + '...')
print('The number is ' + str(roll) + '.')
