# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def ispathsum(root,cursum,target):
            if root is None:
                ##root为空
                return False
            cursum += root.val
            if root.left is None and root.right is None:
                return cursum == target
            return ispathsum(root.left,cursum,target) or ispathsum(root.right,cursum,target)
        ###时间复杂度为树的遍历，O(logN) 空间复杂度为调用递归栈的高度O(logN)
        return ispathsum(root,0,targetSum)