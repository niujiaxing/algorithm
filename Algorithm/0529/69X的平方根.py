class Solution:
    def mySqrt(self, x: int) -> int:
        def findx(left,right,flag):
            if left >= right:
                if left * left > flag:
                    return left - 1
                else:
                    return left
            cur = (left + right) // 2
            sqcur = cur * cur
            if sqcur == flag:
                return cur
            if sqcur > flag:
                return findx(left,cur-1,flag)
            else:
                return findx(cur + 1,right,flag)
        return findx(0,x,x)
        ##时间复杂度 O（logN）  空间复杂度O(logN)