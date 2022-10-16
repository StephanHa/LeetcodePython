# 5. 最长回文子串（中等）
# https://leetcode.cn/problems/longest-palindromic-substring/
# 给你一个字符串 s，找到 s 中最长的回文子串。

# 方法1，暴力解法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ""
        if not s:
            return max_str
        if len(s) == 1:
            return s
        for i in range(len(s) - 1):
            sub_str = ""
            for j in range(i, len(s)):
                sub_str += s[j]
                if sub_str == sub_str[::-1] and len(sub_str) > len(max_str):
                    max_str = sub_str
        return max_str

# 执行用时：8504 ms, 在所有 Python3 提交中击败了4.99%的用户
# 内存消耗：15.2 MB, 在所有 Python3 提交中击败了57.45%的用户
# 通过测试用例：140 / 140



# 方法2，中心扩散
# 枚举所有的「回文中心」并尝试「扩展」，直到无法扩展为止，此时的回文串长度即为此「回文中心」下的最长回文串长度。
# 对所有的长度求出最大值，即可得到最终的答案。
# https://leetcode.cn/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
class Solution2:
    def expandAroundCenter(self, s, left, right) -> str:
        max_str = ""
        sub_str = ""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if left == right:
                sub_str = s[left]
            else:
                sub_str = s[left] + sub_str + s[right]
            if len(sub_str) > len(max_str):
                max_str = sub_str
            left -= 1
            right += 1
        return max_str

    def longestPalindrome(self, s: str) -> str:
        max_str = ""
        if not s:
            return max_str
        if len(s) == 1:
            return s
        for i in range(len(s) - 1):
            # 每个字符串都分别尝试奇数和偶数的回文中心，比较两者获取最长回文子串
            sub1_str = self.expandAroundCenter(s, i, i)
            sub2_str = self.expandAroundCenter(s, i, i+1)
            if len(sub1_str) >= len(sub2_str):
                temp_str = sub1_str
            else:
                temp_str = sub2_str
            if len(temp_str) > len(max_str):
                max_str = temp_str
        return max_str

# 执行用时：988 ms, 在所有 Python3 提交中击败了56.25%的用户
# 内存消耗：15.2 MB, 在所有 Python3 提交中击败了48.67%的用户
# 通过测试用例：140 / 140

# 示例1
# s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。

# 示例2
# s = "cbbd"
# 输出："bb"

# 示例3
s = "ccc"
# 输出："ccc"

# 提示：
# 1 <= s.length <= 1000
# s仅由数字和英文字母组成

test = Solution()
print(test.longestPalindrome(s))
