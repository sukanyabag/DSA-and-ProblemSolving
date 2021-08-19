'''
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
Note that you need to maximize the answer before taking the mod and not after taking it.

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Constraints:
The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sols = {}
        
    def tree_sum(self,node):
        if node == None:
            return 0
        if node in self.sols:
            return self.sols[node]
        res = node.val + self.tree_sum(node.left) + self.tree_sum(node.right)
        
        self.sols[node] = res
        return res
    
    def allSum(self,node,total,res):
        if node == None:
            return res 
        left_sum = self.tree_sum(node.left)
        right_sum = self.tree_sum(node.right)
        res.add(min(left_sum, total-left_sum))
        res.add(min(right_sum, total-right_sum))
        
        self.allSum(node.left, total,res)
        self.allSum(node.right, total,res)
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = self.tree_sum(root)
        
        max_prod = 0
        
        for val in self.sols.values():
            cur = val * (total-val)
            
            if cur > max_prod:
                max_prod = cur
        return max_prod % (1000000000 + 7)
        
