# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
#
# 输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011中，共有三位为 '1'。

# 提示：输入必须是长度为 32 的 二进制串 。

# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xn1m0i/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def hammingWeight(self, n: int) -> int:
        nums = "".join(bin(n)[2:].split("0"))
        return len(nums)


# 执行用时：24 ms, 在所有 Python3 提交中击败了99.58%的用户
# 内存消耗：14.7 MB, 在所有 Python3 提交中击败了77.08%的用户
# 通过测试用例：601 / 601

