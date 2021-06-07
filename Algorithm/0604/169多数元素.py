class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict()
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in nums:
            if i in dic:
                dic[i] += 1
                if  dic[i] > n // 2:
                    return i
            else:
       #时间复杂度 O（N）  空间O（N）