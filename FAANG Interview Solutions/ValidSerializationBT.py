'''
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. 
If it is a null node, we record using a sentinel value such as '#'.

Example 1:
Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

Example 2:
Input: preorder = "1,#"
Output: false

Constraints:
1 <= preorder.length <= 104
preorder consist of integers in the range [0, 100] and '#' separated by commas ','.
'''

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # the basic intuition is to collapse the entire tree into the root node.
        p = preorder.split(',')
        
        stack = []
        
        for s in p:
            stack.append(s)
            # imagine popping from stack as folding of the tree
            while len(stack) > 1 and stack[-1] == '#' and stack[-2] == '#':
                stack.pop()
                stack.pop()
                if not stack:
                    return False
                #by replacing the top with hash you are shrinking tree's 
                #child to null because you already process the child and all it's children
                stack[-1] = '#'
        return stack == ['#']
