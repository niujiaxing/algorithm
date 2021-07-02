class Solution:
    def translateNum(self, num: int) -> int:
        ## 写出状态转移方程
        ## 如果后两位在10-25之间dp(n) = dp(n-1) + dp(n-2)
        ## 如果后两位 <10 或 >25 dp(n) = dp(n-1)
        ## 递归终止条件 dp[0] = 0,dp[1] = 0 
        ## 求dp(n)只需要保存dp(n-1),dp(n-2)
        numstr = str(num)
        if num == 0:
            return 1
        first = 1
        second = 1
        for i in range(len(numstr)-1):
            if int(numstr[i:i+2]) >= 10 and int(numstr[i:i+2]) <= 25:
                first,second = second,first + second
            else:
                first,second = second,second
        return second
        ## 时间复杂度 O（N）
        ## 空间复杂度 O（1）