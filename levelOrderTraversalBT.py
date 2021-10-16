class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])        
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans
        
