'''
Chief's bot is playing an old DOS based game. There is a row of buildings of different heights arranged at each index along a number line. 
The bot starts at building  and at a height of . You must determine the minimum energy his bot needs at the start so that he can jump to the 
top of each building without his energy going below zero.

Units of height relate directly to units of energy. The bot's energy level is calculated as follows:
If the bot's  is less than the height of the building, his 

newEnergy = botEnergy - (height - botEnergy)

If the bot's  is greater than the height of the building, his

newEnergy = botEnergy + (botEnergy - height)

Function Description
Complete the chiefHopper function in the editor below.
chiefHopper has the following parameter(s):
int arr[n]: building heights
Returns
int: the minimum starting. 

Input Format
The first line contains an integer , the number of buildings.
The next line contains  space-separated integers , the heights of the buildings.

Sample Input 0
5
3 4 3 2 4
Sample Output 0
4
Explanation 0
If initial energy is 4, after step 1 energy is 5, after step 2 it's 6, after step 3 it's 9 and after step 4 it's 16, finally at step 5 it's 28.
If initial energy were 3 or less, the bot could not complete the course.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def chiefHopper(arr):
    # Write your code here
    min_energy = 0
    
    for i in range(len(arr)-1, -1, -1):
        min_energy = math.ceil((min_energy + arr[i]) / 2)
    return min_energy

'''
INTUITION - Instead of iterating from start (0 index), if we just iterate from the end and assume that the final bot energy is 0,
then taking final energy as 0 ensures that we will have minimum energy at the start.

As energy update formula is given as

newEnergy = botEnergy + (botEnergy - height)

Solving above equation for botEnergy, we get

botEnergy = (newEnergy + height ) / 2

Taking ceil(next highest integer val), as we are moving backwards.

Using the formula energy = ceil (( arr[i] + energy ) / 2 ), we calculate the energy at each building. 
In this way, we can reach the 1st building (at 0 index) and we get the minimum energy required.

Time Complexity - O(n)
Space Complexity - O(1)
'''
