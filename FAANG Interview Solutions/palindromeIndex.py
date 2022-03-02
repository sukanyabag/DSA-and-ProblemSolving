'''
Given a string of lowercase letters in the range ascii[a-z], determine a character that can be removed to make the string a palindrome. 
There may be more than one solution, but any will do. For example, if your string is "bcbc", you can either remove 'b' at index  or 'c' at index . 
If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.

Function Description

Complete the palindromeIndex function in the editor below. It must return the index of the character to remove or .

palindromeIndex has the following parameter(s):

s: a string to analyze
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a query string .

Output-
return index to be removed to make the str a palindrome
'''

def palindromeIndex(s):
    # Write your code here
    
    #if palindrome check
    if s == s[::-1]:
        return -1
    
    n = len(s)
    
    for i in range(n//2):
        #comparing 1st el with last el
        if s[i] != s[n-1-i]:
            #check if rest of str is palindrome except last elm
            #from end check
            if s[i:n-1-i] == s[i:n-1-i][::-1]:
                #return idx of curr last elm
                return n-1-i
            #check if rest of str is palindrome except 1st elm 
            #from the beg check
            elif s[i+1:n-i] == s[i+1:n-i][::-1]:
                #return idx of curr 1st elm
                return i
    return -1
                
