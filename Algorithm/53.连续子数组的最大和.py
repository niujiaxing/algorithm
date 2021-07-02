class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        reslist = [] ##存放以n结尾的和最大连续子数组的和，最后的结果为max(reslist)
        reslist.append(nums[0])  ## 状态转移方程 f(n) = max(f(n-1)+nums[n],nums[n])
        for i in range(1,len(nums)):
            res = max(reslist[i-1]+nums[i],nums[i])
            reslist.append(res)
        return max(reslist)
        ## 时间复杂度O（N）
        ## 空间复杂度O（1）