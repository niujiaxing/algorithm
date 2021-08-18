# KMP算法

**字符串匹配算法，可以查找在txt字符串中pat字符串出现的位置**

- 可以将暴力算法的O（M*N）时间复杂度降到 O（N）

## KMP过程

```
## ascii 码到127，所以取128
dp[j][c] = next
0 <= j < M，代表当前的状态
0 <= c < 128，代表遇到的字符（ASCII 码）
0 <= next <= M，代表下一个状态

dp[4]['A'] = 3 表示：
当前是状态 4，如果遇到字符 A，
pat 应该转移到状态 3

dp[1]['B'] = 2 表示：
当前是状态 1，如果遇到字符 B，
pat 应该转移到状态 2

```

- 1. 用双重循环写出pat的状态转移矩阵dp【状态】【字符】
- - 需要用到影子状态进行回退，回退到最大匹配状态
- 2. 用txt去匹配，状态 = dp【状态】【当前字符】


##leetcode习题

[28. 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/)

实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

 

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

 

示例 1：

输入：haystack = "hello", needle = "ll"
输出：2
示例 2：

输入：haystack = "aaaaa", needle = "bba"
输出：-1
示例 3：

输入：haystack = "", needle = ""
输出：0


```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ##KMP
        ## 定义一个状态矩阵
        ## dp[状态][字符]
        M = len(needle)
        if M == 0:
            return 0
        dp = [[0 for i in range(128)]for j in range(M)]
        X = 0 ## 影子状态
        dp[0][ord(needle[0])] = 1
        for i in range(1,M):
            for j in range(128):
                dp[i][j] = dp[X][j]
            dp[i][ord(needle[i])] = i + 1 ## 进入下一状态
            X = dp[X][ord(needle[i])]

        ## search
        K = 0
        for i in range(len(haystack)):
            K = dp[K][ord(haystack[i])]
            if K == M:
                return i - M + 1
        return -1


```
