class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ## 采用DFS依次向下搜索
        ## 依次遍历每一个节点，找到最小公共祖先节点
        if root is None or root == p or root == q:
            return root
        ## 利用树的后序遍历找到最小公共祖先
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left is None and right is None:
            return None
        elif left and right:
            return root
        elif left is  None:
            return right
        elif right is None:
            return left
        ## 时间复杂度 O（N）
        ## 空间复杂度 O(N)