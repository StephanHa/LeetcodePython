# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnhbqj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，双指针
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, (len(s) - 1)
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


s = ["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
test = Solution()
print(test.reverseString(s))

# 执行用时：44 ms, 在所有 Python3 提交中击败了70.45%的用户
# 内存消耗：19.6 MB, 在所有 Python3 提交中击败了30.45%的用户
# 通过测试用例：477 / 477
