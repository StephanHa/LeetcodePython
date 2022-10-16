# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#
# 如果反转后整数超过 32 位的有符号整数的范围[−2^31, 2^31− 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/xnx13t/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def reverse(self, x: int) -> int:
        nums = list(str(x))
        if nums[0] == "-":
            nums[1:] = reversed(nums[1:])
        else:
            nums[:] = reversed(nums[:])
        result = int("".join(nums))
        if result < -2**31 or result > 2**31:
            return 0
        else:
            return result


# x = 123
# 输出：321
x = -123
# 输出：-321
test = Solution()
print(test.reverse(x))

# 执行用时：40 ms, 在所有 Python3 提交中击败了58.64%的用户
# 内存消耗：14.8 MB, 在所有 Python3 提交中击败了79.64%的用户
# 通过测试用例：1032 / 1032
