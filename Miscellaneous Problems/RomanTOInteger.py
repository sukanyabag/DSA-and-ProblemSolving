'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
           }
        
        prenum = 0
        sumtot = 0
        
        for i in s[::-1]:
            currnum = roman_dict[i]
            
            #check if prenum > currnum
            if(prenum > currnum):
                sumtot -= currnum
                
            #otherwise add currnum to sumtot
            else:
                sumtot += currnum
                #update prenum to currnum for next iterations
                prenum = currnum
            
        return sumtot
            
'''
For 'IV'
I= 1 and V = 5 
"I" is before "V", we subtract the value of "I" so the value of "IV" = 4

Now let's take a look at the backwards approach:
When we reverse "IV" we get the string "VI"

Note: we need to add the roman values as well as keeping the same rules of "I" before "V"
When we go backwards, we can safely assume that the next "I" value is subtracted since we reversed the string. 
(as long as the previous value is smaller than the current value)

But how do we know when to subtract?
We cant be subtracting every time we see an "I"

We need to keep track of the previous roman value
This is where prenum=currnum comes in
When we loop through the string, prenum=currnum sets the current roman numeral so when we move to the next value, 
we are able to track that previous roman value and determine if that value should be added or subtracted.

In this case, prenum="V" and the next element would be "I"(currnum)
We would subtract the "I" value and continue until we finish looping through the string
prenum=currnum just keeps track of the pointer to the previous roman value to make sure the next roman letter before it follows the 
+/- rule for roman numeral
'''
