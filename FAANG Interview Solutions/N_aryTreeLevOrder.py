'''
Given an n-ary tree, return the level order traversal of its nodes' values.Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        l = defaultdict(list)
        
        def dfs(node, level):
            if not node:
                return
            l[level].append(node.val)
            for ch in node.children:
                dfs(ch, level+1)
                
        dfs(root,0)
        
        return [lst for k,lst in l.items()]
        
