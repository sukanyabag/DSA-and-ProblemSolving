'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; 
and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.

Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Constraints:
1 <= g.length <= 3 * 104
0 <= s.length <= 3 * 104
1 <= g[i], s[j] <= 231 - 1
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sort in descending order to give the 
        # largest cookie to the most greedy kid
        g.sort(reverse = True)
        s.sort(reverse = True)
        
        #init count to 0
        #this at the end returns the max number of children who 
        #will recieve cookies
        count = 0
        
        #init two pointers i and j
        # i traverses greed of children (g) and j traverses cookie size(s)
        i = 0
        j = 0
        
        #either we give cookie to the most greedy child (if he is content)
        #otherwise we move to the next child
        while(i < len(g) and j < len(s)):
            if(s[j] >= g[i]):
                i += 1
                j += 1
                greedfactor += 1
                
            else:
                i += 1
                
        return greedfactor
            
