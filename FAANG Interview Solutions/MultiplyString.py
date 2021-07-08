'''
Q- Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''
#code
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        op = []
        iszeroleading = True
        a = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1,-1):
            for j in range(len(num2)-1, -1,-1):
                val = int(num1[i]) * int(num2[j]) + a[i+j+1]
                a[i+j] += val // 10
                a[i+j+1] = val % 10
        for i in range(len(a)):
            if a[i] != 0:
                iszeroleading = False
            if iszeroleading == False :
                op.append(str(a[i]))
        if op == []:
            return '0'
        return ''.join(op)
                              
                             
            
