class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        dic = dict()
        dic['('] = ')'
        dic['{'] = '}'
        dic['['] = ']'
        stack = []
        ##是否需要不足两个的情况
        for i in range(n):
            cur = s[i]
            if cur in dic:
                stack.append(cur)
            else:
                if len(stack) == 0:
                    return False
                if dic[stack.pop()] != cur:
                    return False
        if len(stack) != 0:
            return False
        return True
