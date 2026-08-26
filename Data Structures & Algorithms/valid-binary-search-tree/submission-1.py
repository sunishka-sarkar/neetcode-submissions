# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,low,high):
            if not node:
                return True
            if node.val<=low or node.val>=high:
                return False
            #leftvalid=dfs(node.left,low,node.val)
            #rightvalid=dfs(node.right,node.val,high)
            return dfs(node.left,low,node.val) and dfs(node.right,node.val,high)
        return dfs(root,float("-inf"),float("+inf"))
        