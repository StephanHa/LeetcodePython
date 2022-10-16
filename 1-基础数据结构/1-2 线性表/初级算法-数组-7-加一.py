# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x2cv1c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add_one = True
        i = len(digits) - 1
        while i >= -1 and add_one:
            add_one = False
            if i == -1:
                digits.insert(0, 1)
                break
            if digits[i] < 9:
                digits[i] += 1
                break
            if digits[i] == 9:
                digits[i] = 0
                add_one = True
                i -= 1
        return digits


#digits = [1,9,9]
# 输出：[2,0,0]
digits = [9]
# 输出：【1, 0]

test = Solution()
print(test.plusOne(digits))

# 执行用时：40 ms, 在所有 Python3 提交中击败了41.84%的用户
# 内存消耗：14.8 MB, 在所有 Python3 提交中击败了85.82%的用户
# 通过测试用例：111 / 111
