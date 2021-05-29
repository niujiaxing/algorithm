class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        merge = TreeNode(root1.val + root2.val)
        leftt = self.mergeTrees(root1.left,root2.left)
        right = self.mergeTrees(root1.right,root2.right)
        merge.left = leftt
        merge.right = right
        return merge
        ##时间复杂度O（min(M,N)） 空间复杂度O（min(M,N)） 