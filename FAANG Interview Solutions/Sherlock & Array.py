'''
Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all
elements to the left is equal to the sum of all elements to the right.

Input format-
The first line contains n, the number of elements in the array .
- The second line contains n space-separated integers arr[i]

Sample Input
3
1 2 3
4
1 2 3 3
Sample Output

NO
YES
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    sum_of_arr = sum(arr)
    add = 0
    
    for i in arr:
        if add == sum_of_arr-i-add:
            return 'YES'
        add += i
    return 'NO'
    

