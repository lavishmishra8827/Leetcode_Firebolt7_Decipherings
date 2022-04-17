# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if not root:
            return root
        self.inorder(root.left)
        root.left=None
        self.cur.right=root
        self.cur=root
        self.inorder(root.right)
        
    def increasingBST_internal(self,root):
    ans=self.cur=TreeNode(None)
    return ans.right
    '''
    #Some wrong approach
    def increasingBST_internal(root):
        if not root.left and not root.right:
            return root,root
        if root.left:
            leftmostnode,rightmostnode=self.increasingBST_internal(root.left)
            rightmostnode.right=root
            root=leftmostnode
        if root.right:
            leftmostnode,rightmostnode=self.increasingBST_internal(root.right)
            root.right=leftmostnode
            root=rightmostnode
        return leftmostnode,rightmostnode
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        leftmost,righmost=self.increasingBST_internal(root)
        return leftmost
    '''