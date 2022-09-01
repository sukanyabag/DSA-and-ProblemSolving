'''
Algorithmic Question : Given an array of size n, randomly output all the elements one by one.

For example,

 Input: int[] nums = {1, 2, 3, 4, 2, 1}
 Output: [2,1,1,4,3,2] is one of the outputs. 
 
 Note: duplicates numbers are allowed in input array. 
 
 Expectation: Space 0(1) and Time 0(n).
    
 

Fisher–Yates shuffle Algorithm works in O(n) time complexity. The assumption here is, we are given a function rand() that generates a random number in O(1) time.
The idea is to start from the last element and swap it with a randomly selected element from the whole array (including the last). 
Now consider the array from 0 to n-2 (size reduced by 1), and repeat the process till we hit the first element. 

To shuffle an array a of n elements (indices 0..n-1):
  for i from n - 1 downto 1 do
       j = random integer with 0 <= j <= i
       exchange a[j] and a[i]
       
       '''

from random import randint
 
# A function to generate a random permutation of arr[]
def randomize (arr, n):
    # Start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    for i in range(n-1,0,-1):
        # Pick a random index from 0 to i
        j = randint(0,i+1)
 
        # Swap arr[i] with the element at random index
        arr[i],arr[j] = arr[j],arr[i]
    return arr
 
# Driver program to test above function.
arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
print(randomize(arr, n))


