class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ## 模拟栈的存放
        ## 将pushed中的值读取到stack中
        ## stack顶端的值如果和此时对应的poped 的第i个值相同
        ## 将栈底弹出
        ## 如果弹出的数量和压入的数量相同，则为一组栈序列
        j = 0
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and j < len(pushed) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(pushed)
        ## 时间复杂度 O（N） N为push和pop的长度
        ## 空间复杂度 O（N） 借助辅助站
