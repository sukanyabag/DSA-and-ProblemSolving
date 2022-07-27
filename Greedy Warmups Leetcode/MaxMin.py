'''
You will be given a list of integers,  arr , and a single integer k. You must create an array of length k from elements 
of arr such that its unfairness is minimized. Call that array arr' . 
Unfairness of an array is calculated as = max( arr' ) -  min( arr ' )

Where:
- max denotes the largest integer in arr' .
- min denotes the smallest integer in arr'.

Note: Integers in  may not be unique.

Function Description
Complete the maxMin function in the editor below.
maxMin has the following parameter(s):

int k: the number of elements to select
int arr[n]:: an array of integers
Returns

int: the minimum possible unfairness

Input Format
The first line contains an integer n, the number of elements in array arr.
The second line contains an integer k .
Each of the next n lines contains an integer arr[ i ] where 0  <=  i  < n.

Constraints
2  <=  n  <=  10^5
2  <=  k  <=  n
0   < =   arr[ i ]   <=  10^9

Sample Input 0
7
3
10
100
300
200
1000
20
30

EXPLANATION - Here, k=3 so,
max(10,20,30) - min(10,20,30) = 30 - 10 = 20

Sample Output 0
20
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    i = 0;
    return min(abs(arr[i+k-1] - arr[i]) for i in range(n-k+1))
       

'''
1. Sort the array to make it uniform/consecutive so that all k subgroups will always have the min will as the first
element and the max as the last in that subgroup (the least unfairness will always be found between consecutive differences(ex, 2-1, 4-3 etc)

INTUITION -  the trick is: instead of making all possible groups and calculating max-min, sort them first. 
Then, in the same list [4,3,1,9], NOW sorted - [1 3 4 9], we will only make the following groups (assuming k=2): [1, 3], [3, 4], and [4, 9]. 
The other groups are irrelevant; as they will have a higher max-min because they are not consecutive.

2. To get subgroups we do abs(i-k+1), (+1 to make sure we get exactly k subgroup, if k = 3 and i = 0, 0-3+1 = -2 = abs(-2) = 2 and 2 is exactly the 3rd idx.)

3. Now just find differences between the subgroups - 
[1, 3], [3, 4], and [4, 9] = so 3-1 = 2, 4-3 = 1, 9-4 = 5 
min(2,1,5) is 1 , which is the answer!
'''
