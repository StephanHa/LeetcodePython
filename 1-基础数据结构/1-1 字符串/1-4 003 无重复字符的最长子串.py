# 3. 无重复字符的最长子串（中等）
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

# 方法1，暴力破解
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        if not s:
            return result
        length = len(s)
        for i in range(length):
            while len(s[i:i+result+1]) == len(set(s[i:i+result+1])) and (i+result) < length:
                result += 1
        return result

# 执行用时：164 ms, 在所有 Python3 提交中击败了16.34%的用户
# 内存消耗：15.2 MB, 在所有 Python3 提交中击败了24.83%的用户
# 通过测试用例：987 / 987


# 方法2，集合去重
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_num = 0
        if not s:
            return max_num
        for i in range(len(s)):
            result = set(s[i])
            j = i + 1
            # 空格也算字符串
            while j < len(s) and s[j] not in result:
                result.add(s[j])
                j += 1
            if max_num < len(result):
                max_num = len(result)
        return max_num


# 执行用时：508 ms, 在所有 Python3 提交中击败了8.38%的用户
# 内存消耗：15.2 MB, 在所有 Python3 提交中击败了19.36%的用户
# 通过测试用例：987 / 987


# 方法3，滑动窗口
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/






# 示例1
s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 示例2
# s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是"b"，所以其长度为1。

# 示例3
# s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"wke"，所以其长度为3。
# 请注意，你的答案必须是子串的长度，"pwke"是一个子序列，不是子串。

# 示例4
# s = " "
# 输出1

test = Solution2()
print(test.lengthOfLongestSubstring(s))
