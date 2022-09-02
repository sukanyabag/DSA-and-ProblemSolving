'''
PROBLEM = A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

We can rotate digits of a number by 180 degrees to form new digits.

Note that after rotating a number, we can ignore leading zeros.

For example, after rotating 8000, we have 0008 which is considered as just 8.

Given an integer n, return the number of confusing numbers in the inclusive range [1, n].

Example 1:

Input: n = 20 Output: 6 Explanation: The confusing numbers are [6,9,10,16,18,19]. 6 converts to 9. 9 converts to 6. 
10 converts to 01 which is just 1. 16 converts to 91. 18 converts to 81. 19 converts to 61.
orig = 19 

rot = 61

if we add 1 to ori's right
191 -> 19 * 10 + 1

newrot = 161

so newrot is 161 -> 10^2 + rot = 100 + 61 = 161

ori = 81
rot = 18
if we add 1 to ori's right
811 -> 81 * 10 + 1

new rot = 118

new rot = 10^2 + rot = 100 + 18 = 118


orig(19)
rot(61)
n(2)
if we append a dig x(1) to the right of orig value(191), the new 
number becomes orig*10+x = 19 * 10 + 1= 191, and the newrot(161)
is exactly 10^(n*x) + rot = 10**(2*1) + 61 = 161

'''
def confusingNO(self, N:int) -> int:
	dict= {0:0, 1:1, 6:9, 8:8, 9:6}
	
	def helper(ori, rot, mult):
		res = 0
		if ori != rot:
			res += 1
		for d in dict:
			if ori==0 and d==0:
				continue
			if ori*10 + d <= N:
				res += helper(ori*10 + d, dict[d]*mult + rot, mult*10)
		return res

	return helper(0,0,1)
		
