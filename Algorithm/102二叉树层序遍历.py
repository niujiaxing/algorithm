# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        curlist = []
        treedeque = deque()
        ##将树中的节点依次压入队列，弹出时压入左右子树
        if root:
            treedeque.append(root)
            while len(treedeque) != 0:
                cursize = len(treedeque)
                ###层序遍历
                for i in range(cursize):
                    treenode = treedeque.popleft()
                    curlist.append(treenode.val)
                    ### 多叉树可以在这里加入for循环                    
                    if treenode.left:
                        treedeque.append(treenode.left)
                    if treenode.right:
                        treedeque.append(treenode.right)
                res.append(curlist[:])
                curlist.clear()
        return res
        ## 时间复杂度 O(N)
        ## 空间复杂度O(N)