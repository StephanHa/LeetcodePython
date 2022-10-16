# 位异或运算，相同为0，不同为1
# 1 ^ 4 = 5, bin(1)="0b1", bin(4)="0b100", bin(5)="0b101"


# 两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
# 给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
#
# 输入：x = 1, y = 4
# 输出：2
# 解释：
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# 上面的箭头指出了对应二进制位不同的位置。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnyode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法1，位异或运算
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = bin(x ^ y)[2:]
        result = len("".join(num.split("0")))
        return result


x = 1
y = 4
test = Solution()
print(test.hammingDistance(x, y))

# 执行用时：36 ms, 在所有 Python3 提交中击败了70.71%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了55.75%的用户
# 通过测试用例：149 / 149

