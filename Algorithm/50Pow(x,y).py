class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x ** n
        ## 将n转化成2进制 
        res = 1
        
        if n < 0:
            n = -n
            x = 1/x
        b = x
        while n > 0:            
            if n & 1:
                res = res * b ## 计算
            b *= b ## 从第一位开始与
            n >>= 1 ## n每次右移一位
        return res

        ## 时间复杂度 O(logN) 对n进行二进制拆分
        ## 空间复杂度 O(1)
