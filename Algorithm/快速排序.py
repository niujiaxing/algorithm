import random
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        ## 快速排序进行排序，然后找出前k个数
        ## 快速排序，哨兵选择和递归
        def quicksort(arr,left,right):
            ## left,right为排序范围，闭区间
            ## 哨兵划分要随机
            if right <= left:
                return 
            # num = random.randint(left,right)
            # arr[num],arr[left] = arr[left],arr[num]
            i,j = left,right
            while i < j:
                
                while i<j and arr[j] >= arr[left]: j-= 1
                while i<j and arr[i] <= arr[left]: i += 1
                arr[i],arr[j] = arr[j],arr[i]
            print(arr[i],arr[j],arr[left])
            arr[j] , arr[left] = arr[left],arr[j]
            quicksort(arr,left,j-1)
            quicksort(arr,j+1,right)
            return
        quicksort(arr,0,len(arr)-1)
        return arr[:k]