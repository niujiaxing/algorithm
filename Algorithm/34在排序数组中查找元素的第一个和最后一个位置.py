class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ###复杂度O（N）
        ##1.找到第一个target和最后一个target的位置，记录左右位置
        res = []
        left = -1
        right = -1
        for i in range(len(nums)):
            if nums[i] == target and left == -1:
                left = i
                right = i
            elif nums[i] == target and left != -1:
                right = i
        res.append(left)
        res.append(right)
        return res
