class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = [0 for i in range(n+1)]
        miss = 0
        ## cnt【i】 表示该数组中存在几个i
        ## miss可以看作连续n个数的空缺
        for i in arr:
            cnt[min(i,n)] += 1
        for i in cnt[1:]:
            if i == 0 :
                miss += 1
            else:
                ## 弥补之前的空缺
                miss -= min(i-1,miss)
        ## 时间复杂度O（N）  空间复杂度O（N）
        return n-mis