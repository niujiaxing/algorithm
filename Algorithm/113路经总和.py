class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.res = []
        self.path = []
        def preodertravel(self,root,targetSum):
            if not root:                
                return
            
            self.path.append(root.val)
            if not root.left and not root.right and sum(self.path) == targetSum:                
                self.res.append(self.path[:])
            preodertravel(self,root.left,targetSum)            
            preodertravel(self,root.right,targetSum)
            self.path.pop()
            
        if root:
            preodertravel(self,root,targetSum)

        return self.res
        ## 时间复杂度 O（N2） 空间复杂度O（N）