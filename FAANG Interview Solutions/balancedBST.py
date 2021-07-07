# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #helper
        def helper_func(currNode):
            if not currNode:
                return (0, True) #tuple -> (height, check_if_balanced)
            
            left_height, left_balanced = helper_func(currNode.left)
            right_height, right_balanced = helper_func(currNode.right)
            return (max(left_height,right_height)+1, left_balanced and right_balanced and 
                  abs(left_height - right_height) <= 1 )
        
            
        return helper_func(root)[1] #note - [1] as we are interested in boolean val & not height
