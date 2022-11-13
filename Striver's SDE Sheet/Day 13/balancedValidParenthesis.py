'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Input: s = "(]"
Output: false
 
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        brace_dict = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char not in brace_dict:
                stck.append(char)
                continue
            if not stck or stck[-1] != brace_dict[char]:
                return False

            stck.pop()

        return True if not stck else False
