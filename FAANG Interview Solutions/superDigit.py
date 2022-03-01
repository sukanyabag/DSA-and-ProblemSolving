'''
the super digit of  will be calculated as:

	super_digit(9875)   	9+8+7+5 = 29 
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2  
Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):
string n: a string representation of an integer
int k: no of repetitions

Returns
int: the super digit of n repeated k times
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    if len(n) == 1 and k == 1:
        return int(n)
    total =  str(sum([int(d) for d in n])) * k
    return superDigit(total, 1)
