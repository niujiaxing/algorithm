class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ##常规转圈法
        road = [[0,1],[1,0],[0,-1],[-1,0]] #右下左上，进行遍历
        res = []
        def inlist(x,y,matrix):
            if x < 0 or x > len(matrix)-1:
                return False
            if y < 0 or y > len(matrix[0])-1:
                return False
            return True

        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            visited = [[0] * len(matrix[0]) for i in range(len(matrix))]
            vistnum = 0,turn = 0,x = 0,y = 0
            while vistnum != m * n :
                if inlist(x,y,matrix) and not visited[x][y]:
                    res.append(matrix[x][y])
                    visited[x][y] = 1
                    vistnum += 1
                else:
                    x -= road[turn%4][0]
                    y -= road[turn%4][1]
                    turn += 1
                x += road[turn%4][0]
                y += road[turn%4][1]
        return res
##时间复杂度时间复杂度：O(mn)
# 空间复杂度：O(mn) visited记录是否访问