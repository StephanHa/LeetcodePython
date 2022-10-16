#
# 给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
# 如果needle 不是 haystack 的一部分，则返回 -1 。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnr003/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，暴力破解
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1


# haystack = "sadbutsad"
# needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。

# haystack = "leetcode"
# needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。

# haystack = "hello"
# needle = "ll"

haystack = "a"
needle = "a"
test = Solution()
print(test.strStr(haystack, needle))


# 执行用时：40 ms, 在所有 Python3 提交中击败了44.18%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了51.93%的用户
# 通过测试用例：79 / 79
