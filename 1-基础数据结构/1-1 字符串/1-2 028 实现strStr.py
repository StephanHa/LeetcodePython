# 28. 实现 strStr() （简单）
# https://leetcode.cn/problems/implement-strstr/
# 实现strStr()函数。
# 给你两个字符串haystack和needle，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
# 如果不存在，则返回 -1 。
#
# 说明：
# 当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 对于本题而言，当needle是空字符串时我们应当返回 0 。这与 C 语言的strstr()以及 Java 的indexOf()定义相符。

# 方法1，暴力破解
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        length = len(needle)
        for index in range(len(haystack) - length + 1):
            if haystack[index:index + length] == needle:
                return index
        return -1


# 示例1
# haystack = "hello"
# needle = "ll"
# 输出：2

# 示例2
haystack = "aaaaa"
needle = "bba"
# 输出：-1

test = Solution()
print(test.strStr(haystack, needle))

# 执行用时：36 ms, 在所有 Python3 提交中击败了72.35%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了47.07%的用户
# 通过测试用例：76 / 76
