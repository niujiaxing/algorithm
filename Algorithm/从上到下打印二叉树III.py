# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root:
            treedeque = deque() ##对二叉树进行层序遍历的队列
            treedeque.append(root)            
            while len(treedeque) != 0:
                count = len(treedeque)
                curlist = [] ## 定义临时存放每层的遍历结果
                for i in range(count):
                    curnode = treedeque.popleft()
                    curlist.append(curnode.val) ##将该层遍历所得到的值存放在curlist
                    if curnode.left:
                        treedeque.append(curnode.left)
                    if curnode.right:
                        treedeque.append(curnode.right)
                    ## 将左右节点拉入双端队列                
                if len(res) % 2 == 0:
                    res.append(curlist) ## 用切片而不可以直接压入，因为临时变量要反复使用
                else:
                    res.append(curlist[::-1])
                ## 单层则逆序压入
        return res
        ## 时间复杂度O（N）总共对N个节点进行操作
        ## 空间复杂度 O(N)