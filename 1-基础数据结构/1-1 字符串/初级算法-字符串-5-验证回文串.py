# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。
# 则可以认为该短语是一个 回文串 。
# 字母和数字都属于字母数字字符。
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xne8id/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，直接遍历获取字母和数字
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for item in s:
            # 如果字符是数字或字母，则加入result字符（字母先转小写再加入）
            if item.isdigit():
                result += item
            elif item.isalpha():
                result += item.lower()
        if result == result[::-1]:
            return True
        else:
            return False


# 执行用时：72 ms, 在所有 Python3 提交中击败了9.84%的用户
# 内存消耗：15.4 MB, 在所有 Python3 提交中击败了58.25%的用户
# 通过测试用例：480 / 480


# 方法2，双指针
# 左右同时遍历，只要不相同，则返回False，如果全部遍历完，则返回True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = s.lower()
        # 如果字符是数字或字母，则加入result字符
        result = "".join([x for x in news if x.isdigit() or x.isalpha()])
        left, right = 0, (len(result) - 1)
        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
        return True


# s = "A man, a plan, a canal: Panama"
# 输出：true
# 解释："amanaplanacanalpanama" 是回文串。

s = "race a car"
test = Solution()
print(test.isPalindrome(s))

# 执行用时：44 ms, 在所有 Python3 提交中击败了88.37%的用户
# 内存消耗：15.9 MB, 在所有 Python3 提交中击败了42.04%的用户
# 通过测试用例：480 / 480
