'''
Tree problem – A tree node can either be an internal node or a leaf node.
If it is an internal node then it stores the sum of lengths of strings present in its left and right child.
If it is a leaf node then it stores string as well as its length.

A cord tree is a binary tree of strings.
A node in this tree can be a leaf node or an internal node.
An internal node has two children, a left child and a right child. It also has a length of all the children under it
A leaf nodes have a value and a length

Given input is above tree and N when You have to return the Nth character present in the tree.

#                                      InternalNode, 26
                                #      /              \   
                                #     /                \                         
                                #    /                  \
                                # Leaf(5, ABCDE)      InternalNode, 21
                                #                       /           \
                                #                      /             \
                                #                     /               \
                                #                    /                 \
                                #         Leaf(10, FGHIJKLMNO)     Leaf(11, PQRSTUVWXYZ)  
'''

class CordTree:
  def __init__(self,root):
    self.root = root
    
class InternalNode:
  def __init__(self,left,right,length):
    self.left = left;
    self.right = right;
    self.length = length;
    
class LeafNode:
  def __init__(self,length,val):
    self.length = length
    self.val = val
    
# this function returns null if the index is out of range
def findCharAtIdx(root,idx):
  #base case
  if not root or idx < 0:
    return None
  
  elif isInstance(root,InternalNode):
    # assumes that we will never have an InternalNode at a leaf
    if not root.left or not root.right:
      return findCharAtIdx(root.left or root.right, idx)
    
    else:
      left = root.left
      right = root.right
      
      search = None
      
      if idx < left.length:
        search = left
      
      else:
        search = right
        idx -= left.length
        
      return findCharAtIdx(search,idx)
    
    else:
      return root.val[idx] if idx < root.length \
        else None
      
