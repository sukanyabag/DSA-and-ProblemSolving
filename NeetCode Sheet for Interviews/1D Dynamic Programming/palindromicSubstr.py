'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''

#TWO POINTER APPROACH
class Solution:
    '''
    TC - O(N^2) (N for odd expansion, N for even expansion of left and right pointers)
    SC - O(1)
    '''
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            #odd length palindromes
            l = r = i
            res += self.countPali(s,l,r)

            #even length palindromes
            l = i
            r = i+1
            res += self.countPali(s,l,r)
        return res



    def countPali(self,s,l,r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

        return res

#DYNAMIC PROGRAMMING APPROACH (NOT REQD, just ico curiosity)
'''
A DP solution to this problem is to build a table with all possible string[start:end] combinations,
storing which are palindromes and which are not (True or False). At any given moment, when you're 
checking if string[i:j] is a palindrome, you only need to know two things:

Is string[i] equal to string[j]?
Is string[i+1:j-1] a palindrome?
For condition (1), a simple check might do, for condition (2), you use the table. If both conditions are met,
mark table[i][j] as True and increase your count.

TC - O(N^2)
SC - O(N^2)
'''

def countSubstrings(self, s):
    if not s:
        return 0

    n = len(s)
    table = [[False for x in range(n)] for y in range(n)]
    count = 0

    # Every isolated char is a palindrome
    for i in range(n):
        table[i][i] = True
        count += 1

    # Check for a window of size 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            table[i][i+1] = True
            count += 1

    # Check windows of size 3 and more
    for k in range(3, n+1):
        for i in range(n-k+1):
            j = i+k-1
            if table[i+1][j-1] and s[i] == s[j]:
                table[i][j] = True
                count += 1

    return count
