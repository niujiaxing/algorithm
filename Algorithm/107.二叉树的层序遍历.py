from collections import deque 
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ## 自顶向下遍历，最后一步反转链表
        res = []
        res_ = [] ## 保存每一层层序遍历结果
        curres = deque() ## 进行层序遍历的队列

        if root:
            curres.append(root)
            while curres: 
                n = len(curres)
                for _ in range(n):
                    i = curres.popleft()
                    if i.left:
                        curres.append(i.left)
                    if i.right:
                        curres.append(i.right)
                    res_.append(i.val)
                res.append(res_[:])
                # print(res)
                res_.clear()
        return res[::-1]
        ## 时间复杂度O（N）
        ## 空间复杂度O（N）