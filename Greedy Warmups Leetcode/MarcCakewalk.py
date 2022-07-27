'''
Problem link - https://www.hackerrank.com/challenges/marcs-cakewalk/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    # Write your code here
    calorie.sort(reverse = True)
    return sum(calorie[i]*2**i for i in range(len(calorie)))
    
'''
LOGIC - As you eat more cupcakes the 2 to the power of i multiplier becomes larger. If you start larger you 
end up multiplying the large numbers by smaller 2 power i values minimizing the miles. So simply we reverse sort and calculate!
'''
