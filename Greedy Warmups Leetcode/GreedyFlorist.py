'''
A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new customers and the money he makes. 
To do this, he decides he'll multiply the price of each flower by the number of that customer's previously purchased flowers plus 1. 
The first flower will be original price, ( 0 + 1 ) * original price , the next will be  ( 1 + 1 ) * original price and so on.

Given the size of the group of friends, the number of flowers they want to purchase and the original prices of the flowers,
determine the minimum cost to purchase all of the flowers.

Function Description
Complete the getMinimumCost function in the editor below. It should return the minimum cost to purchase all of the flowers.

getMinimumCost has the following parameter(s):
c: an array of integers representing the original price of each flower
k: an integer, the number of friends
Input Format
The first line contains two space-separated integers n and k, the number of flowers and the number of friends.
The second line contains n space-separated positive integers c[ i ] , the original price of each flower.

Constraints
1  <=  n. k  <= 100
1  <=  c[ i ]  <=  10^6
answer  <   2^31
0   <=  i  <  n

Output Format
Print the minimum cost to buy all n flowers.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

'''
If A and B go to buy flowers [1,2,7,9,100], then the minimum price is 130. Why?
Assume only one person buys the flowers in the given order. So, she pays (1)1+(2)2+(3)7+(4)9+(5)100 = 562. 
From this we can see that order matters; for example, if she buys them in the opposite order, we get (1)100+(2)9+(3)7+(4)2+(5)1 = 152!
Even without a second person, we can see that an opportunistic order drastically improves the price. Hence we sort the array of prices/cost in 
descending order.

So, hopefully without giving the problem away, what we would want to do is assign the flowers to A and B in such a way not only 
to reduce the total number each person purchases [so that no person will buy an ith flower larger than is necessary (so that their ith multiplyer 
will be no larger than is necessary for any given flower)], but to assign the order they buy their flowers responsibly as well.

Note: the order of the people does not affect the price, only the order of flowers purchased by each person.
Intuition - you can keep a track of purchases of individual customers in an array by initialising default 
values with zero and access them by %k in iteration of cost loop.
'''

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    mincost = 0;
    c.sort(reverse = True);
    benefit = 1
    
    for i in range(len(c)):
        mincost += c[i] * benefit
        if (i+1) % k == 0:
            benefit += 1
            
    return mincost
        
        
