class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ##zip实现矩阵转置
        ###投机取巧法
        res = []
        while matrix:
            lis = list(matrix.pop(0))##弹出第一行
            for i in lis:
                res.append(i) 
            print(res)
            ####将矩阵翻转后继续
            matrix = list(zip(*matrix))[::-1]
        return res