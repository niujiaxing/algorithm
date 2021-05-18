class Solution:
    def climbStairs(self, n: int) -> int:
        ##类似斐波那契数列
        ##爬到第n层有两种方式，从n-1层爬一级和从n-2层爬两级
        ###fn = fn-1 + fn-2
        ###循环更快
        ###边界条件
        if n < 3:
            return n
        a = 1
        b = 2
        for i in range(3,n+1):
            a,b = b,a+b
        return b