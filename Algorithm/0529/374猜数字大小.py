class Solution:
    def guessNumber(self, n: int) -> int:
        def findn(left,right):
            cur = (left + right) // 2
            gus = guess(cur)
            if gus == 0:
                return cur
            if gus == -1:
                return findn(left,cur-1)
            if gus == 1:
                return findn(cur+1,right)
        return findn(1,n)