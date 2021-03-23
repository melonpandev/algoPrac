# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def isMirror(self, leftTree: TreeNode, rightTree: TreeNode) -> bool:
        if leftTree == None and rightTree == None:
            return True
        elif leftTree == None or rightTree == None:
            return False
        return (leftTree.val == rightTree.val) and self.isMirror(leftTree.left,rightTree.right) and self.isMirror(leftTree.right, rightTree.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
