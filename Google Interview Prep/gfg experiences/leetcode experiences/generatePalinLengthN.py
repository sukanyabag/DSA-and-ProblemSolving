'''
Check if a string is palindrome or not.
Given, a number 'n' generate all palindromes of that length.
Given the number n, find all mirror imaged palindromes (consisting of digits {1-9} only) from length 1 to length 'n'.
Here mirror image palindrome referred to flipping the numer, i.e., 101 as well as 609 is considered a palindrome.


NOT YET COMPLETED
'''

# Python implementation of the approach
 
# Function to return the
# reverse of num
def reverse(num):
    rev = 0;
    while (num > 0):
        rev = rev * 10 + num % 10;
        num = num // 10;
 
    return rev;
 
# Function that returns true
# if num is palindrome
def isPalindrome(num):
    # If the number is equal to the
    # reverse of it then it
    # is a palindrome
    if (num == reverse(num)):
        return True;
 
    return False;
 
# Function to print all the
# d-digit palindrome numbers
def printPalindromes(d):
 
    if (d <= 0):
        return;
 
    # Smallest and the largest d-digit numbers
    smallest = pow(10, d - 1);
    largest = pow(10, d) - 1;
 
    # Starting from the smallest d-digit
    # number till the largest
    for i in range(smallest, largest + 1):
 
        # If the current number
        # is palindrome
        if (isPalindrome(i)):
            print(i, end = " ");
 
# Driver code
d = 2;
 
printPalindromes(d);
