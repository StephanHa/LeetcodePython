# 1143. 最长公共子序列（中等）
# https://leetcode.cn/problems/longest-common-subsequence/
#
# 给定两个字符串text1 和text2，返回这两个字符串的最长公共子序列的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
#
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

# 示例1
# text1 = "abcde"
# text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。

# 示例2
text1 = "abc"
text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。

# 示例3
# text1 = "abc"
# text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。

# 测试用例
text1 = "ezupkr"
text2 = "ubmrapg"
# 输出：2

# 方法1，动态规划
# https://leetcode.cn/problems/longest-common-subsequence/solution/fu-xue-ming-zhu-er-wei-dong-tai-gui-hua-r5ez6/
# dp[i][j]定义为text1[0:i-1]和text2[0:j-1]的最长公共子序列
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

# 执行用时：332 ms, 在所有 Python3 提交中击败了93.10%的用户
# 内存消耗：22.9 MB, 在所有 Python3 提交中击败了71.66%的用户
# 通过测试用例：45 / 45


text = Solution()
print(text.longestCommonSubsequence(text1, text2))

