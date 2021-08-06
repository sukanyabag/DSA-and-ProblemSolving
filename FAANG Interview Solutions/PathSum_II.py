'''
Problem - 
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.
A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Input: root = [1,2,3], targetSum = 5
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, sum_tot, l, res):
        if root.left is None and root.right is None:
            if root.val == sum_tot:
                res += [l + [root.val]]
        if root.left:
            self.helper(root.left, sum_tot-root.val, l + [root.val], res)
        if root.right:
            self.helper(root.right, sum_tot-root.val, l + [root.val], res)
            
        return res
    
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        return self.helper(root, targetSum, [], [])
