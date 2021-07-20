class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ## 对二叉树进行前序遍历
        ## 在从前序遍历的结果构建链表
        if not root:
            return root
        self.list = []
        def preodertravel(self,root):
            if root:
                self.list.append(root)
                preodertravel(self,root.left)
                preodertravel(self,root.right)
            return 
        preodertravel(self,root)
        if len(self.list) == 1:
            return self.list[0]
        for i in range(1,len(self.list)):
            pre = self.list[i-1]
            pre.left = None
            pre.right = self.list[i]
        self.list[-1].left,self.list[-1].right = None,None
        return self.list[0]
        ## 时间复杂度O（N） 空间复杂度O（N）