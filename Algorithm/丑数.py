class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ###状态转移方程2，3，5的最小倍数
        a,b,c = 0,0,0
        dp = []
        dp.append(1)
        
        for i in range(n):
            dp.append(min(2*dp[a],3*dp[b],5*dp[c]))
            if 2*dp[a] == dp[-1]:
                a += 1
            if 3*dp[b] == dp[-1]:
                b += 1
            if 5*dp[c] == dp[-1]:
                c += 1
        return dp[n-1]
        ## 时间复杂度O（N）
