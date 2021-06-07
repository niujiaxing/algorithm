class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchm(i,j,matrix,target):
            m = len(matrix)
            if i >= m:
                return False
            if j < 0:
                return False
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                return searchm(i,j-1,matrix,target)
            else:
                return searchm(i+1,j,matrix,target)
        return searchm(0,len(matrix[0])-1,matrix,target)
        ##先和第一行最右边值比较，可以排除一行或一列，最多比较 M+N 次可以得到结果
        #时间复杂度 O(n+m)O(n+m)  空间复杂度 O(1)
