class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        ## python的 and 操作如果最后结果为真，返回最后一个表达式的值，or 操作如果结果为真，返回第一个结果为真的表达式的值
        ## 短路，将ConditionA && ConditionB  Condition A为 False 则不成立，利用该条件终止循环
        return n and (n + self.sumNums(n-1))
        ## 时间复杂度 O（N）
        ## 空间复杂度 O（N）