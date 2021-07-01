class Solution:
    def myAtoi(self, s: str) -> int:
        ###正则表达式
        INT_MAX = 2147483647    
        INT_MIN = -2147483648
        s = s.lstrip()
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(s) 
        if len(num) == 0:
            return 0
        num = int(num[0]) #由于返回的是个列表
        return max(min(num,INT_MAX),INT_MIN)    #返回值
