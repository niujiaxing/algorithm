class Solution:
    def fib(self, n: int) -> int:
        ## 非递归，循环写法
        ## n重循环需要计算n-2次
        if n < 1:
            return 0
        first = 0
        second = 1
        for i in range(n-1):
            first,second = second,first + second
        return second % 1000000007
        ## 时间复杂度O（N）
        ## 空间复杂度O（1）